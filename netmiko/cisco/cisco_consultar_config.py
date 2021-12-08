from netmiko import ConnectHandler
#from getpass import getpass

IP_LIST = open('ip_switch.txt')

for ip_device in (IP_LIST):
    print(f'Consultando: {ip_device}')
    RTP ={'device_type':'cisco_ios','ip':ip_device,'username':'admin','password':'senha','secret':'senha'}
    net_connect = ConnectHandler(**RTP)
    net_connect.enable()

    # Buscar comando
    print('#### CONFIG logging host ####')
    print('#### show start ####')
    output = net_connect.send_command('sh start | inc logging host')
    print(output)

    print('#### show run ####')
    output = net_connect.send_command('sh run | inc logging host')
    print(output)

    print('#### CONFIG SNMP ####')
    print('#### show start ####')
    output = net_connect.send_command('sh start | inc snmp-server host')
    print(output)

    print('#### show run ####')
    output = net_connect.send_command('sh run | inc snmp-server host')
    print(output)
    print('##############################################################')

    net_connect.disconnect()

print('Fim de Execucao do Script')
