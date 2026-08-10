from netmiko import ConnectHandler

class routers_ssh:
    def __init__(self, router, connect):
        self.r_ssh = router
        self.connected = connect

    def sent_comm(self):
        
        print(f"connected to {self.r_ssh['host']}")
        
        connection = ConnectHandler(**self.r_ssh)
        print(connection.send_command(self.connected))

        connection.disconnect()



for i in range(11, 14):
    routers = {
        'device_type': 'mikrotik_routeros',
        'host': f'10.10.10.{i}',
        'username': 'admin',
        'password': '123456'
    }
    A = routers_ssh(routers, f"/system identity print")
    A.sent_comm()
