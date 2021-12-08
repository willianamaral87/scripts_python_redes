import getpass
import telnetlib

HOST = "192.168.7.100"

user = input("Enter your telnet username: ")
#user = "willian"

password = getpass.getpass()
#password = "willian"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"config t\n")

for n in range (30,1001):
    tn.write(b"no vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"Name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    print(f'Criando VLAN  {n}')


tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

