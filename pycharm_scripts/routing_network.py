class routers_ssh:
    def __init__(self, router, connect):
        self.r_ssh = router
        self.connect = connect


    def sent_comm(self):
        print(f"\nconnected to {self.r_ssh["host"]}")
        print(self.r_ssh)



for i in range(11, 14):
    routers = {
        'type_device': 'mikrotik_routeros',
        'host': f'10.10.10.{i}',
        'username': 'admin',
        'password': '123456'
    }
    A = routers_ssh(routers, "/system identity print")
    A.sent_comm()

