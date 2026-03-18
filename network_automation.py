from netmiko import ConnectHandler

devices = [{
    "device_type": "cisco_ios",
    "host": "192.168.221.2",
    "username": "admin",
    "password": "cisco",
},
{
    "device_type": "cisco_ios",
    "host": "192.168.221.3",
    "username": "admin",
    "password": "cisco",
}, ]

for device in devices:
    print(f'\n Connecting to {device["host"]}...')
    connection = ConnectHandler(**device)
    output = connection.send_command("show ip interface brief")
    print(output)
    connection.disconnect()
    print(f'Disconnected from {device['host']}')
