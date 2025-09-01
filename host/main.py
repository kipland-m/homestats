# Kipland Melton 2025
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.responses import PlainTextResponse
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

@app.get("/get-stats")
async def get_stats(request: Request):
    query = agent_stats.select().order_by(desc(agent_stats.c.id)).limit(10)

    results = await database.fetch_all(query)
    
    if not results:
        return {'agents': [], 'message': 'No data available'}
    
    agents_data = []
    for row in results:
        agents_data.append({
            'id': row['id'],
            'timestamp': str(row['timestamp']) if row['timestamp'] else 'N/A',
            'ip_address': row['ip_address'],
            'mac_address': row['mac_address'],
            'cpu_cores': row['cpu_cores'],
            'cpu_threads': row['cpu_threads'],
            'memory_gb': row['memory_gb'],
            'disk_gb': row['disk_gb'],
            'bytes_sent': row['bytes_sent'],
            'bytes_recv': row['bytes_recv']
        })
    
    return {'agents': agents_data, 'count': len(agents_data)}

@app.post("/receive-stats")
async def receive_stats(request: Request):
    data = await request.json()

    hardware = data["hardware"]
    network = data["network"]

    print("Hardware:", hardware)
    print("Network:", network)

    query = agent_stats.insert().values(
         cpu_cores=hardware["cpu_cores"],
         cpu_threads=hardware["cpu_threads"],
         memory_gb=hardware["memory_gb"],
         disk_gb=hardware["disk_gb"],
         ip_address=network["ip_address"],
         mac_address=network["mac_address"],
         bytes_sent=network["bytes_sent"],
         bytes_recv=network["bytes_recv"]
     )

    await database.execute(query)

    return {'received': 'data stored successfully'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


