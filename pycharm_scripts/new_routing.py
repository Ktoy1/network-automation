from netmiko import ConnectHandler

class Router:
    def __init__(self, host, user, passw):
        self.host = host
        self.username = user
        self.password = passw

    def connect(self):
        return ConnectHandler(
            device_type = "mikrotik_routeros",
            host = self.host,
            username = self.username,
            password = self.password
        )

    def identity(self):
        connection = self.connect()

        try:
            return connection.send_command(
                "/system identity print"
            )

        finally:
            connection.disconnect()
    def add_ip(self, interface, sub_address):
        connection = self.connect()

        try:
            command = (
                f"/ip address"
                f" add address={sub_address}"
                f"interface=ether{interface+1} "

            )
            return connection.send_command(command)
        finally:
            connection.disconnect()
    def routing(self, routes):
        connection = self.connect()

        try:
            for i in routes:

                command = (
                    f"/ip route add "
                    f"dst-address={i['distination']} "
                    f"gateway={i['gateway']}"
                )

                print(connection.send_command(command))
        finally:
            connection.disconnect()

for i in range(11, 14):
    router = Router(
            f"10.10.10.{i}",
            "admin",
            "123456"
    )
    router.identity()
    for sub in range(1, 8):
        if i == 11:
            router.add_ip(sub, f"192.168.{sub}.1/24")
        elif i == 12:
            router.add_ip(sub, f"192.168.{sub+20}.1/24")
        else:
            router.add_ip(sub, f"192.168.{sub+40}.1/24")

    routes = [
        {
            'distination': '192.168.32.0/19',
            'gateway': '10.10.10.13'

        },
        {
            'distination': '192.168.16.0/20',
            'gateway': '10.10.10.12'
        },
        {
         'distination': '192.168.0.0/20',
         'gateway': '10.10.10.11'
        },
        {
            'distination': '192.168.32.0/19',
            'gateway': '10.10.10.13'
        },
        {
            'distination': '192.168.0.0/20',
            'gateway': '10.10.10.11'
        },
        {
            'distination': '192.168.16.0/20',
            'gateway': '10.10.10.12'
        }


    ]


    router.routing(routes)

