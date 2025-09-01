# Kipland Melton 2025

import requests
import psutil
from psutil import Process
import socket
import time
from datetime import datetime
import os
import sys
import time
import dotenv 
import netifaces

dotenv.load_dotenv()

connected_clients = set()
host = os.getenv("host")

def get_hardware_info():
    hardware_info = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_cores": psutil.cpu_count(logical=False),
        "cpu_threads": psutil.cpu_count(logical=True),
        "memory_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "disk_gb": round(psutil.disk_usage('/').total / (1024**3), 2)
    }

    return hardware_info

def get_network_info():
    addrs = psutil.net_if_addrs()
    stats = psutil.net_io_counters()

    try:
         current_process = psutil.Process(os.getpid())
         connections = current_process.net_connections(kind='inet')

         print(connections)
    except psutil.AccessDenied:
         print("Need elevated permissions for network connections")
         connections = []

    ip_address = None
    mac_address = None

    for interface, addresses in addrs.items():
        for addr in addresses:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip_address = addr.address
            elif addr.family == psutil.AF_LINK:
                mac_address = addr.address

    network_info = {
        "ip_address": ip_address,
        "mac_address": mac_address,
        "bytes_sent": stats.bytes_sent,
        "bytes_recv": stats.bytes_recv
        }

    return network_info


def main():
    while True:
        try:
            network_info = get_network_info()
            hardware_info = get_hardware_info()

            if len(sys.argv) == 1:
                print("Did you specify intervals (seconds)?")

            if len(sys.argv) < 2:
                print("Usage: \n\tpython3 agent.py <int seconds>")
                return 0;
            
            interval_seconds = int(sys.argv[1])

            system_info = {
                "hardware": hardware_info,
                "network": network_info
            }

            print("sending system info |", datetime.now())

            requests.post(f'http://{host}:8000/receive-stats', json=system_info)
            time.sleep(interval_seconds)

        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()
