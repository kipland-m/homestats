from flask import Flask, request
from flask_socketio import SocketIO, emit 

app = Flask(__name__)
socketio = SocketIO(app)

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

#    server = await websockets.serve(handle_client, 'localhost', 12345)
#    await server.wait_closed()

@app.route('/receive_hardware_data', methods=['POST'])
def receive_hardware_data():
    data = request.json

    print("Received hardware data:", data)
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
