from netmiko import ConnectHandler

ip_address = ['10.10.10.11', '10.10.10.12', '10.10.10.13']

for i in ip_address:
    
    routers = {'device_type': 'mikrotik_routeros',
            'host': i,
            'username': 'admin',
            'password': '123456',
            }
    connection = ConnectHandler(**routers)
    print(connection.send_command("/system identity print"))
    

