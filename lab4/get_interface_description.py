from netmiko import ConnectHandler

# Routers
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}
r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

routers = (r1, r2, r3)

# List of show commands to run
show_commands = [
    "show ip interface brief",
    "show interface description",
    "show version",
    "show running-config | include hostname"
]

for device in routers:
    print(f"\nConnecting to {device['ip']}...")
    try:
        net_connect = ConnectHandler(**device)
        for cmd in show_commands:
            print(f"\n>>> {cmd}")
            output = net_connect.send_command(cmd)
            print(output)
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")

