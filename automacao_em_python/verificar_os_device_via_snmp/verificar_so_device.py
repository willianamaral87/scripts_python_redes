# Importar modulo do sistema operacional
import subprocess

# Identificador de cada fabricante
vendor_nexus = 'Cisco NX-OS'
vendor_cisco = 'Cisco IOS Software'
vendor_enterasys = 'Enterasys'
vendor_extreme = 'Extreme'
vendor_huawei = 'Huawei'
vendor_hp = 'HP'

devices_nexus = []
devices_cisco = []
devices_huawei = []
devices_enterasys = []
devices_hp = []
devices_others = []

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Abrir o arquivo contendo os hosts que serão configurados
alldevices = open('lista_devices.txt')

# Recuperar e tratar cada host do arquivo
for device in (alldevices):
   print('-------------')
   print(f'Device :{device}')

   device = device.rstrip()

   cmd = ['snmpwalk', '-v2c', '-c', 'cwfadr7H3s', device, 'sysDescr.0']
   proc1 = subprocess.run(cmd, stdout=subprocess.PIPE)
   print(proc1.stdout)

   # Converter a saida do snmpwak de bytes para string
   saida_snmpwalk = proc1.stdout.decode("utf-8")

   if vendor_nexus in saida_snmpwalk:
      print('NEXUS')
      devices_nexus.append(device)
   elif vendor_cisco in saida_snmpwalk:
      print('CISCO IOS')
      devices_cisco.append(device)
   elif vendor_enterasys in saida_snmpwalk or vendor_extreme in saida_snmpwalk:
      print('Enterasys ou Extreme')
      devices_enterasys.append(device)
   elif vendor_huawei in saida_snmpwalk:
      print('Huawei')
      devices_huawei.append(device)
   elif vendor_hp in saida_snmpwalk:
      print('HP')
      devices_hp.append(device)
   else:
      print('nao identificado')
      devices_others.append(device)

print('##### RESUMO #####')

print('NEXUS')
for i in devices_nexus:
    print(i)
print()

print('CISCO')
for i in devices_cisco:
    print(i)
print()

print('HUAWEI')
for i in devices_huawei:
    print(i)
print()

print('ENTERASYS')
for i in devices_enterasys:
    print(i)
print()

print('HP')
for i in devices_hp:
    print(i)
print()



print('NAO IDENTIFICADOS')
for i in devices_others:
    print(i)
print()

