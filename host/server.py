from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_hardware_data', methods=['POST'])
def receive_hardware_data():
    data = request.json

    print("Received hardware data:", data)
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
