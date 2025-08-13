# Kipland Melton 2025

import requests
import psutil
import socket
import time
import os
import time
import dotenv 
import netifaces

dotenv.load_dotenv()

connected_clients = set()
host = os.getenv("host")

def get_hardware_info():
    hardware_info = {
        "cpu_cores": psutil.cpu_count(logical=False),
        "cpu_threads": psutil.cpu_count(logical=True),
        "memory_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "disk_gb": round(psutil.disk_usage('/').total / (1024**3), 2)
    }

    return hardware_info

def get_network_info():
    addrs = psutil.net_if_addrs()
    stats = psutil.net_io_counters()

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
    print(f"host ip: {host}")

    while True:
        try:
            network_info = get_network_info()
            hardware_info = get_hardware_info()

            # Combine into one
            system_info = {
                "hardware": hardware_info,
                "network": network_info
            }

            print(system_info["hardware"])
            print("\n\n\n")
            print(system_info["network"])

            response = requests.post(f'http://{host}:8000/receive-stats', json=system_info)
            print(response.text)
                
            time.sleep(10)

        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()
