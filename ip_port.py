from netmiko import ConnectHandler
router = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.24.11',
    'username': 'admin',
    'password': '123456'
    }

connection = ConnectHandler(**router)
print(connection.send_command("/system identity print"))

data = {
    'ip_address': '192.168.23.1/24',
    'port': 'ether5'  
    }
for key, value in data.items():
    print(connection.send_command(f"/ip address add address={data['ip_address']}, interface={data['port']}"))