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

        # Тухайн interface дээрх хуучин IP-г устгана
        remove = f"/ip address remove [find interface={interface}]"

        # Шинэ IP нэмнэ
        command = f"/ip address add address={address} interface={interface}"

        print(connection.send_command(remove))
        print(f"{interface} дээрх хуучин хаяг цэвэрлэгдлээ")

        print(connection.send_command(command))
        print(f"{interface} дээр шинэ {address} IP амжилттай нэмэгдлээ")

    connection.disconnect()