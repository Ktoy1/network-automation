
ip_address = ['192.168.24.11', '192.168.23.1', '192.168.30.1'] 

for i in ip_address:
    
    routers = {'device_type': 'mikrotik_routeros',
            'host': i,
            'username': 'admin',
            'password': '123456',
            }

    print(routers)