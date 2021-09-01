from time import sleep
import re

# Lista conteudo o arquivo de configuracao
lista = []

#### NOME DO ARQUIVO xxxx ENDERECO IP ####


######################## ALTERAR O NOME ARQUIVO ########################
with open('output_cisco/processados/saida_arquivo.log', 'r') as tex:
    for linha in tex:
        # Armanzer cada linha do arquivo em uma posição da lista
        lista.append(linha.strip())    
tex.close()  

print('###############################')

######################## ALTERAR O IP #######################
endereco_IP = '10.22.252.254'
IP_LIST = []
IP_LIST.append(endereco_IP)



######################################################################################
################ ENVIAR CONFIGURACAO PARA OS EQUIPAMENTOS ############################
######################################################################################

from netmiko import ConnectHandler
#from getpass import getpass

for routers in (IP_LIST):
    print(f'Configurando IP: {routers}')
    RTP ={'device_type':'cisco_ios','ip':routers,'username':'admin','password':'senha','secret':'senha'}
    net_connect = ConnectHandler(**RTP)
    net_connect.enable()

    ########## COMANDOS DE CONFIGURACAO ###########
    configurar = net_connect.send_config_set(lista)
    
    ########### SALVAR A CONFIGURACAO ###########
    # salvar = ['do write memory']
    # configurar = net_connect.send_config_set(salvar)

    ########### DESCONECTAR ###########
    net_connect.disconnect()

print('Fim Script')
