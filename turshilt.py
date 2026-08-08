router = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.24.11',
    'username': 'admin',
    'password': '123456'
    }

data = {
    'ip_address': '192.168.23.1/24',
    'port': 'ether5'  
    }
print(type(data['ip_address']))
print(type(data['port']))