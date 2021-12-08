import getpass
import telnetlib

HOST = "192.168.7.100"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"config t\n")
tn.write(b"hostname Switch\n")
#tn.write(b"ip address 3.1.1.1 255.255.255.255\n")


#tn.write(b"int loop 4\n")
#tn.write(b"ip address 5.2.2.2 255.255.255.255\n")

#tn.write(b"do wr\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

