for i in range(11, 14):
    
    routers = {'device_type': 'mikrotik_routeros',
            'host': f'10.10.10.{i}',
            'username': 'admin',
            'password': '123456',
            }
    print(routers)