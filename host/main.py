"""
██╗  ██╗ ██████╗ ███╗   ███╗███████╗███████╗████████╗ █████╗ ████████╗███████╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
███████║██║   ██║██╔████╔██║█████╗  ███████╗   ██║   ███████║   ██║   ███████╗
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ╚════██║   ██║   ██╔══██║   ██║   ╚════██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗███████║   ██║   ██║  ██║   ██║   ███████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝

                  ◯ Retro Monitoring Dashboard  ◯
                  ▫ Real-time system metrics     ▫
                  ▫ Multi-agent data collection  ▫
                  ▫ Built with FastAPI & SQLite  ▫

# Kipland Melton 2025
# FastAPI backend for collecting and serving system stats from network agents
# Features: SQLite storage, real-time updates, lightweight retro-themed frontend
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from host.models import AgentData, AgentResponse, StatsResponse
import uvicorn
from sqlalchemy import desc

from host.db import database, agent_stats

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],  # frontend origin
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
async def handle_client(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        connected_clients.remove(websocket)

    server = await websockets.serve(handle_client, 'localhost', 12345)
    await server.wait_closed()
"""


@app.get("/get-stats", response_model=StatsResponse)
async def get_stats(request: Request):
    query = agent_stats.select().order_by(desc(agent_stats.c.id)).limit(10)

    results = await database.fetch_all(query)
    
    if not results:
        return {'agents': [], 'message': 'No data available'}
    
    agents_data = [
        AgentResponse(
            id=row["id"],
            timestamp=row["timestamp"],
            ip_address=row["ip_address"],
            mac_address=row["mac_address"],
            cpu_cores=row["cpu_cores"],
            cpu_threads=row["cpu_threads"],
            cpu_percent=row["cpu_percent"],
            memory_gb=row["memory_gb"],
            disk_gb=row["disk_gb"],
            bytes_sent=row["bytes_sent"],
            bytes_recv=row["bytes_recv"],
        )
        for row in results
    ]
    
    return StatsResponse(agents=agents_data, count=len(agents_data))

@app.post("/receive-stats")
async def receive_stats(request: AgentData):

    hardware = request.hardware
    network = request.network

    print("Hardware:", hardware)
    print("Network:", network)

    from datetime import datetime
    query = agent_stats.insert().values(
          timestamp=datetime.now(),
          cpu_cores=hardware.cpu_cores,    
          cpu_threads=hardware.cpu_threads,
          memory_gb=hardware.memory_gb,
          disk_gb=hardware.disk_gb,
          cpu_percent=hardware.cpu_percent,
          ip_address=network.ip_address,
          mac_address=network.mac_address,
          bytes_sent=network.bytes_sent,
          bytes_recv=network.bytes_recv
    )

    await database.execute(query)

    return {'received': 'data stored successfully'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


