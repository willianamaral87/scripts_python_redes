
import getpass
import telnetlib

HOST = "192.168.7.102"

#user = input("Enter your telnet username: ")
user = "willian"

#password = getpass.getpass()
password = "willian"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"config t\n")
tn.write(b"vlan 10\n")
tn.write(b"name VLAN_Python_10\n")

tn.write(b"vlan 11\n")
tn.write(b"name VLAN_Python_11\n")

tn.write(b"vlan 12\n")
tn.write(b"name Vlan_Python_12\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

