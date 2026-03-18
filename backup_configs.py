import os
from datetime import datetime
from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.221.2",
        "username" : "admin",
        "password" : "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.221.3",
        "username" : "admin",
        "password" : "cisco",
    },
]
hostnames = ["R1", "R2"]

backup_folder = "backups"
os.makedirs(backup_folder, exist_ok=True)

date = datetime.now().strftime("%Y-%m-%d_%H-%M")

for device, hostname in zip(devices, hostnames):
    print(f'Connecting to {hostname}...')
    connection = ConnectHandler(**device)
    output = connection.send_command("show running-config")
    filename = f'{backup_folder}/{hostname}_{date}.txt'
    with open(filename, "w") as f:
        f.write(output)
    print(f'config saved to {filename}')
    connection.disconnect()

print('\nAll backup complete!')