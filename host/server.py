# Kipland Melton 2025
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

# Allow requests from browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
async def receive_hardware_data(request: Request):
    return {'data': 'successfully reached backend'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
