from netmiko import ConnectHandler
for i in range(11, 14):
    
    routers = {'device_type': 'mikrotik_routeros',
            'host': f'10.10.10.{i}',
            'username': 'admin',
            'password': '123456',
            }
    connection = ConnectHandler(**routers)
    print(connection.send_command("/system identity print"))
    
    for ip in range(1, 8):
        connection.send_command(f"/ip address add address=192.168.{ip}.1/24 interface=ether{ip+1}")

