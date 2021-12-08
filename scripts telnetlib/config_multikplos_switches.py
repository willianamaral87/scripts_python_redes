from netmiko import ConnectHandler
"""
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.7.104',
    'username': 'switch4',
    'password': 'switch4'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.7.105',
    'username': 'switch5',
    'password': 'swtch5'
}
"""
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.7.106',
    'username': 'amaral',
    'password': 'amaral'
}

#all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

all_devices = [iosv_l2_s3]

print(all_devices)

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print(devices)
    for n in range (300,500):
       #print(devices)
       print ("DELETING VLAN " + str(n))
       #config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       config_commands = ['no vlan ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
