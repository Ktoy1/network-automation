from netmiko import ConnectHandler

class Router:
    def __init__(self, device, host, user, passw):
        self.device = device
        self.host = host
        self.username = user
        self.password = passw

    def get_connect(self):
        return ConnectHandler(
            device_type = 'mikrotik_routeros',
            host = self.host,
            username = self.username,
            password =  self.password
        )

    def get_config(self, subnets):
        try:
            connect_router = self.connect()
            connect_router.send_command(f'/system identity set name={self.device}', expect_string=r'>')
            print(connect_router.send_command('system identity print'))

            if self.device in subnets:
                ether = 1
                for ip in subnets[self.device]:
                    ether += 1
                    connect_router.send_command(f'/ip address add address={ip}'
                                                f'interface={ether}'
                                                )

        finally:
            connect_router.disconnect()

    def get_routing(self, route):
        try:
            connect_routing = self.connect()
            for routers in route:
                for dst in route[routers]:

                    connect_routing.send_command(f'/ip route add dst-address={dst} gateway={routers[dst]}')

        finally:
            connect_routing.disconnect()




management = {}
subnets = {}
route = {
    'router1':{'10.10.10.12':'192.168.16.0/20',
               '10.10.10.13': '192.168.0.0/18',
               '10.10.10.14': '192.168.32.0/19',
               '10.10.10.15': '192.168.48.0/20',
               '10.10.10.16': '192.168.0.0/17',
               '10.10.10.17': '192.168.64.0/20'},

    'router2':{'10.10.10.11':'192.168.0.0/19',
               '10.10.10.13': '192.168.0.0/18',
               '10.10.10.14': '192.168.32.0/19',
               '10.10.10.15': '192.168.48.0/20',
               '10.10.10.16': '192.168.0.0/17',
               '10.10.10.17': '192.168.64.0/20'},
    'router3': {'10.10.10.12': '192.168.16.0/20',
                '10.10.10.11': '192.168.0.0/19',
                '10.10.10.14': '192.168.32.0/19',
                '10.10.10.15': '192.168.48.0/20',
                '10.10.10.16': '192.168.0.0/17',
                '10.10.10.17': '192.168.64.0/20'},

    'router4': {'10.10.10.11': '192.168.0.0/19',
                '10.10.10.13': '192.168.0.0/19',
                '10.10.10.12': '192.168.0.0/20',
                '10.10.10.15': '192.168.48.0/20',
                '10.10.10.16': '192.168.0.0/17',
                '10.10.10.17': '192.168.64.0/20'},
    'router5':{'10.10.10.11':'192.168.0.0/19',
               '10.10.10.13': '192.168.0.0/18',
               '10.10.10.14': '192.168.32.0/19',
               '10.10.10.12': '192.168.16.0/20',
               '10.10.10.16': '192.168.0.0/17',
               '10.10.10.17': '192.168.64.0/20'},
    'router6': {'10.10.10.12': '192.168.16.0/20',
                '10.10.10.11': '192.168.0.0/19',
                '10.10.10.14': '192.168.32.0/19',
                '10.10.10.15': '192.168.48.0/20',
                '10.10.10.13': '192.168.0.0/18',
                '10.10.10.17': '192.168.64.0/20'},

    'router7': {'10.10.10.11': '192.168.0.0/19',
                '10.10.10.13': '192.168.0.0/19',
                '10.10.10.12': '192.168.0.0/20',
                '10.10.10.15': '192.168.48.0/20',
                '10.10.10.16': '192.168.0.0/17',
                '10.10.10.14': '192.168.32.0/19'}
}

for i in range(1, 8):
    device_name = f'router{i}'
    management[device_name] = [f'10.10.10.{10+i}', 'admin', '123456']
    subnets[device_name] = [f'192.168.{(i*10)+ip}.1/24' for ip in range(1, 8)]

for ss in management:
    router = Router(
        ss,
        management[0],
        management[1],
        management[2]
    )
    #router.get_config(subnets)
    router.get_routing(route)


