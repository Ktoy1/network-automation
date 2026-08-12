from netmiko import ConnectHandler   # netmiko сангаас ConnectHandler-ийг импортлох

# Router-т зориулсан класс үүсгэх
class Router:
    # ssh-д зориулсан method үүсгэх
    def __init__(self, host, user, passw):
        self.host = host
        self.username = user
        self.password = passw

    # төхөөрөмжид холбогдох method
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

        # портууд дээр ip хаяг бичих команд method
    def add_ip(self, interface, sub_address):
        connection = self.connect()

        try:
            return connection.send_command(f"/ip address add address={sub_address} interface=ether{interface+1}")

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
    

    #портуудад ip хаяг өгөх for давтамж 
    for sub in range(1, 8):
        if i == 11:
            router.add_ip(sub, f"192.168.{sub}.1/24")
        elif i == 12:
            router.add_ip(sub, f"192.168.{sub+20}.1/24")
        else:
            router.add_ip(sub, f"192.168.{sub+40}.1/24")

     router.identity()
    # статик маршрут бичих cidr хаягууд болон тус бүрийн gateway-үүд
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
