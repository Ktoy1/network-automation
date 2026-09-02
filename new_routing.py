import json as js
from netmiko import ConnectHandler

class RouterNetwork:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def get_ssh(self):

        return ConnectHandler(
            device_type='mikrotik_routeros',
            host = self.host,
            username = self.username,
            password = self.password,
        )

    def get_ip_routing(self, ip_addresses, static_route):
        connect_config = None
        try:
            connect_config = self.get_ssh()
            for interface, ip_address in ip_addresses.items():
                connect_config.send_command(f'/ip address add address={ip_address} interface={interface}')
            for gateway, subnets in static_route.items():
                connect_config.send_command(f'/ip route add dst-address={subnets} gateway={gateway}')
        finally:
            if connect_config:
                try:
                    connect_config.disconnect()
                except Exception:
                    # шаардлагатай бол лог бичээрэй
                    print("холболтын алдаа")

with open(r"ssh_data.json", "r", encoding="utf-8") as outfile:
    all_data = js.load(outfile)

    for routers, data in all_data.items():
        R = RouterNetwork(data['ssh']['host'],
                          data['ssh']['username'],
                          data['ssh']['password']
                          )
        R.get_ip_routing(
            data['ip_address'],
            data['static_route']
        )
