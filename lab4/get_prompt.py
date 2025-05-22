from netmiko import Netmiko

# List of all network devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # R1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # R2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # SW1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    # Add more devices here as needed
]

# Loop through each device and print prompts
for device in devices:
    try:
        net_connect = Netmiko(**device)
        print(f"\nConnected to {device['ip']}")
        print(f"Default prompt: {net_connect.find_prompt()}")
        
        net_connect.send_command_timing("disable")
        print(f"After disable: {net_connect.find_prompt()}")
        
        net_connect.enable()
        print(f"After enable: {net_connect.find_prompt()}")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['ip']}: {e}")
