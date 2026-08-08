from netmiko import ConnectHandler

router_1 = {'device_type': 'mikrotik_routeros',
            'host': '192.168.24.11',
            'username': 'admin',
            'password': '123456',
            }

router_2 = {'device_type': 'mikrotik_routeros',
            'host': '192.168.23.2',
            'username': 'admin',
            'password': '123456',
            }

for i in range(1, 3):
    if i == 1:
        connection = ConnectHandler(**router_1)
        print(connection.send_command("/system identity print"))
    else:
        connection = ConnectHandler(**router_2)
        print(connection.send_command("/system identity print"))
        