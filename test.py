from netmiko import ConnectHandler
router = {
    'device_type': 'miktotik_routeros',
    'host': '192.168.24.11',
    'username': 'admin',
    'password': '123456'
}
connection = ConnectHandler(**router)
print(connection.send_command("/system identity print"))
connection.disconnect()