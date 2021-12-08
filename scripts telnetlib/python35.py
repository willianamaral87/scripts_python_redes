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

    for n in range (2,500):
        tn.write(b"no vlan " + str(n).encode('ascii') + b"\n")
        #tn.write(b"Name Python_VLAN_" + str(n).encode('ascii') + b"\n")
        #print(f'ADDING  VLAN  {n}')
    tn.write(b"end\n")
    tn.write(b"exit\n")
    tn.write(b"wr\n") 
    print(tn.read_all().decode('ascii'))
