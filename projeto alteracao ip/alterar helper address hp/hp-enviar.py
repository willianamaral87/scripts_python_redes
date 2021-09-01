from time import sleep
import re

# Lista conteudo o arquivo de configuracao
lista = []

#### NOME DO ARQUIVO xxxx ENDERECO IP ####
##############################################################


######################## ALTERAR O NOME ARQUIVO ########################
with open('output_hp/processados/core/core_sw.txt', 'r') as tex:
    for linha in tex:
        # Armanzer cada linha do arquivo em uma posição da lista
        lista.append(linha.strip())
tex.close()

print('###############################')


endereco_IP = 'IP'
IP_LIST = []
IP_LIST.append(endereco_IP)

print(lista)

from netmiko import ConnectHandler
#from getpass import getpass

for routers in (IP_LIST):
    print(routers)
    RTP ={'device_type':'hp_comware','ip':routers,'username':'admin','password':'senha}
    net_connect = ConnectHandler(**RTP)
    net_connect.enable()


########## COMANDOS DE CONFIGURACAO ###########
configurar = net_connect.send_config_set(lista)

########## SALVAR A CONFIGURACAO ###########
# salvar = ['save']
# configurar = net_connect.send_config_set(salvar)


print(configurar)

# salvar = ['do write memory']
# configurar = net_connect.send_config_set(salvar)


print('Fim Script')
