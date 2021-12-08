
#import logging

import netmiko

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.7.106',
    'username': 'amaral',
    'password': 'amaral'
}

net_connect = ConnectHandler(**iosv_l2)

#net_connect = ConnectHandler(**I86BI_LINUXL2-ADVENTERPRISEK9-M)

output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 51', 'ip address 50.50.50.50 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (21,23):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)

output = net_connect.send_config_set('do wr')
print(output)
print('fim')
