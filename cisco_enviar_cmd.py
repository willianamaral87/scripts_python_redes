from netmiko import ConnectHandler
#from getpass import getpass

IP_LIST = open('ip_switch.txt')

for ip_device in (IP_LIST):
    print(f'Configurando: {ip_device}')
    RTP ={'device_type':'cisco_ios','ip':ip_device,'username':'admin','password':'senha','secret':'senha'}
    net_connect = ConnectHandler(**RTP)
    net_connect.enable()

    alterar_logging = ['no logging host IP', 'logging host IP' ]
    configurar = net_connect.send_config_set(alterar_logging)
    
    alterar_snmp = ['no snmp-server host X version 3 priv redes', 'snmp-server host X version 3 priv redes' ]
    configurar = net_connect.send_config_set(alterar_snmp)
    
    salvar = ['do write memory']
    configurar = net_connect.send_config_set(salvar)

    net_connect.disconnect()

print('Fim de Execucao do Script')
