import requests
import psutil
import time
import os
import dotenv 
import netifaces

dotenv.load_dotenv()

host = os.getenv("host")

while True:
    try:
        print(f"host ip: {host}")

        print(netifaces.interfaces(),netifaces.ifaddresses('lo0'))

        hardware_data = {
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent,
            'cpu_freq': psutil.cpu_freq(),
            'bytes_sent': psutil.net_io_counters().bytes_sent,
            'bytes_received': psutil.net_io_counters().bytes_recv,
        }

        response = requests.post(f'http://{host}:5000/receive_hardware_data', json=hardware_data)
        print(response.text)
            
        time.sleep(15)

    except Exception as e:
        print("Error:", e)
