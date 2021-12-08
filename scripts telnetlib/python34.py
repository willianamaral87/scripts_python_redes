import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
#user = "willian"
password = getpass.getpass()
#password = "willian"

f = open('myswitches')

for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + (IP))
    HOST = IP

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"config t\n")

    tn.write(b"vlan 200\n")
    tn.write(b"name Python_VLAN_200\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 300\n")
    tn.write(b"name Python_VLAN_300\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 400\n")
    tn.write(b"name Python_VLAN_400\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 500\n")
    tn.write(b"name Python_VLAN_500\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 600\n")
    tn.write(b"name Python_VLAN_600\n")
    tn.write(b"vlan 700\n")
    tn.write(b"name Python_VLAN_700\n")
    tn.write(b"vlan 800\n")
    tn.write(b"name Python_VLAN_800\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
