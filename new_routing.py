import json as js
from netmiko import ConnectHandler

class RouterNetwork:
    def __init__(self, username, host, password):
        self.username = username
        self.host = host
        self.password = password

    def get_ssh(self):

        return ConnectHandler(
            device_type='mikrotik_routeros',
            host = self.host,
            username = self.username,
            password = self.password,
        )

    def get_ip_routing(self, ip_addresses, static_route):

        try:
            connect_config = self.get_ssh()
            for interface, ip_address in ip_addresses.items():
                connect_config.send_command(f'/ip address add address={ip_address} interface={interface}')
            for gateway, subnets in static_route.items():
                connect_config.send_command(f'/ip route add dst-address={subnets} gateway={gateway}')
        finally:
            connect_config.disconnect()

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


