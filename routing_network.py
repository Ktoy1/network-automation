from netmiko import ConnectHandler


class RoutersSSH:

    def __init__(self, router, command):
        self.router = router
        self.command = command

    def send_comm(self):
        connection = ConnectHandler(**self.router)

        print(f"\nConnected to {self.router['host']}")
        print(connection.send_command(self.command))

        connection.disconnect()


class IPAddress:

    def __init__(self, ip, maska, router):
        self.ip = ip
        self.maska = maska
        self.router = router

    def add_ip(self):

        connection = ConnectHandler(**self.router)

        interface = f"ether{self.ip + 1}"
        address = f"192.168.{self.ip}.{self.maska}/24"

        # Хуучин IP устгах
        remove_command = (f"/ip address remove [find interface={interface}]")

        connection.send_command(remove_command)

        print(f"{interface} дээрх хуучин IP цэвэрлэгдлээ")

        # Шинэ IP нэмэх
        add_command = (f"/ip address add address={address} interface={interface}")

        connection.send_command(add_command)

        print(f"{interface} дээр {address} амжилттай нэмэгдлээ")

        connection.disconnect()


for i in range(11, 14):

    router = {
        'device_type': 'mikrotik_routeros',
        'host': f'10.10.10.{i}', # ip's management
        'username': 'admin',
        'password': '123456'
    }

    # Router-ийн identity шалгах
    A = RoutersSSH(router,"/system identity print")

    A.send_comm()

    # IP тохируулах
    for t in range(1, 8):

        if i == 11:
            A = IPAddress(t, 1, router)

        elif i == 12:
            A = IPAddress(t+50, 1, router)

        else:
            A = IPAddress(t+100, 1, router)

        A.add_ip()