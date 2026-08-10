from netmiko import ConnectHandler

for i in range(11, 14):

    router = {
        'device_type': 'mikrotik_routeros',
        'host': f'10.10.10.{i}',
        'username': 'admin',
        'password': '123456',
    }

    connection = ConnectHandler(**router)

    print(f"\nConnected to 10.10.10.{i}")
    print(connection.send_command("/system identity print"))

    for ip in range(1, 8):
        interface = f"ether{ip + 1}"
        address = f"192.168.{ip}.1/24"

        command = f"/ip address add address={address} interface={interface}"

        print(command)
        print(connection.send_command(command))

    connection.disconnect()