from netmiko import ConnectHandler
router = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.24.11',
    'username': 'admin',
    'password': '123456'
}
connection = ConnectHandler(**router)
print(connection.send_command("/system identity print"))
command = ["/interface print", "/ip address print", "/ip route print", "/ip arp print", "/ip firewall filter print"]
for cmd in command:
    print(connection.send_command(cmd))
connection.disconnect()