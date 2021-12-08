#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def funcao_windows(mac):
    print('MAC no formato Windows:', mac)

    print('\nFormatado para :')
    
    ############# Linux #############   
    mac_dns = mac.lower()
    mac_dns = mac_dns.replace('-',':')
    print('Linux       :', mac_dns)
    
    ############# Windows #############
    mac_windows = mac.upper()
    print('Windows     :', mac_windows)

    ############# HP #############
    mac_hp_aux = list(mac.lower())

    # Remover os - 
    mac_hp_aux.pop(2)
    mac_hp_aux.pop(7)
    mac_hp_aux.pop(12)

    print('HP          : ', end='')
    for i in range(0,len(mac_hp_aux)):
        print(mac_hp_aux[i],end='')

    print(end='\n')

    ############# CISCO #############
    # Converte para minusculo:
    mac_cisco_aux = mac.lower()

    #Cria a lista
    mac_cisco_aux = list(mac_cisco_aux)

    # Remover os - e substituir por .
    mac_cisco_aux.pop(2)
    mac_cisco_aux.pop(7)
    mac_cisco_aux.pop(12)
    mac_cisco_aux[4] = '.'
    mac_cisco_aux[9] = '.'

    print('Cisco       : ', end='')

    for i in range(0,len(mac_cisco_aux)):
        print(mac_cisco_aux[i],end='')

    print(end='\n')

def funcao_linux(mac):
    print('MAC no formato Linux:', mac)
    
    print('\nFormatado para :')
    
    ############# Linux ############# 
    print('Linux       :', mac.lower())

    ############# Windows #############
    mac_windows = mac.upper()
    mac_windows = mac_windows.replace(':','-')
    print('Windows     :', mac_windows)
    
    ############# HP #############
    mac_hp_aux = list(mac.lower())

    # Remover os - 
    mac_hp_aux.pop(2)
    mac_hp_aux.pop(7)
    mac_hp_aux.pop(12)
    mac_hp_aux[4] = '-'
    mac_hp_aux[9] = '-'

    print('HP          : ', end='')
    for i in range(0,len(mac_hp_aux)):
        print(mac_hp_aux[i],end='')

    print(end='\n')
    
    ############# CISCO #############
    mac_cisco_aux = mac.lower()

    #Cria a lista
    mac_cisco_aux = list(mac_cisco_aux)

    # Remover os - e substituir por .
    mac_cisco_aux.pop(2)
    mac_cisco_aux.pop(7)
    mac_cisco_aux.pop(12)
    mac_cisco_aux[4] = '.'
    mac_cisco_aux[9] = '.'

    print('Cisco       : ', end='')

    for i in range(0,len(mac_cisco_aux)):
        print(mac_cisco_aux[i],end='')

    print(end='\n')
    
def funcao_hp(mac):
    print('MAC no formato HP:', mac)
    print('\nFormatado para :')
    
    ############# Linux #############   
    mac_dns = mac.lower()
    mac_linux = []
    mac_linux.append(mac_dns[0])
    mac_linux.append(mac_dns[1])
    mac_linux.append(':')
    mac_linux.append(mac_dns[2])
    mac_linux.append(mac_dns[3])
    mac_linux.append(':')
    mac_linux.append(mac_dns[5])
    mac_linux.append(mac_dns[6])
    mac_linux.append(':')
    mac_linux.append(mac_dns[7])
    mac_linux.append(mac_dns[8])
    mac_linux.append(':')
    mac_linux.append(mac_dns[10])
    mac_linux.append(mac_dns[11])
    mac_linux.append(':')
    mac_linux.append(mac_dns[12])
    mac_linux.append(mac_dns[13]) 

    print('Linux       : ', end='' )
    
    for i in range(0,len(mac_linux)):
        print(mac_linux[i], end='')
    
    ############# Windows #############
    mac_win = mac.upper()
    mac_windows = []
    mac_windows.append(mac_win[0])
    mac_windows.append(mac_win[1])
    mac_windows.append('-')
    mac_windows.append(mac_win[2])
    mac_windows.append(mac_win[3])
    mac_windows.append('-')
    mac_windows.append(mac_win[5])
    mac_windows.append(mac_win[6])
    mac_windows.append('-')
    mac_windows.append(mac_win[7])
    mac_windows.append(mac_win[8])
    mac_windows.append('-')
    mac_windows.append(mac_win[10])
    mac_windows.append(mac_win[11])
    mac_windows.append('-')
    mac_windows.append(mac_win[12])
    mac_windows.append(mac_win[13])     
    
    print('\nWindows     : ', end='' )
    
    for i in range(0,len(mac_windows)):
        print(mac_windows[i], end='')
        
    ############# HP #############
    print('\nHP          :', mac)

    ############# CISCO #############
    mac_cisco = mac[4].replace('-','.')
    
    mac_cisco_aux = mac.lower()

    #Cria a lista
    mac_cisco_aux = list(mac_cisco_aux)

    mac_cisco_aux[4] = '.'
    mac_cisco_aux[9] = '.'

    print('Cisco       : ', end='')

    for i in range(0,len(mac_cisco_aux)):
        print(mac_cisco_aux[i],end='')

    print(end='\n')

def funcao_cisco(mac):    
    print('MAC no formato Cisco:', mac)
    
    print('\nFormatado para :')
    
    ############# Linux #############   
    mac_dns = mac.lower()
    mac_linux = []
    mac_linux.append(mac_dns[0])
    mac_linux.append(mac_dns[1])
    mac_linux.append(':')
    mac_linux.append(mac_dns[2])
    mac_linux.append(mac_dns[3])
    mac_linux.append(':')
    mac_linux.append(mac_dns[5])
    mac_linux.append(mac_dns[6])
    mac_linux.append(':')
    mac_linux.append(mac_dns[7])
    mac_linux.append(mac_dns[8])
    mac_linux.append(':')
    mac_linux.append(mac_dns[10])
    mac_linux.append(mac_dns[11])
    mac_linux.append(':')
    mac_linux.append(mac_dns[12])
    mac_linux.append(mac_dns[13]) 
    
    print('Linux       : ', end='' )
    
    for i in range(0,len(mac_linux)):
        print(mac_linux[i], end='')
        
    ############# Windows #############
    mac_win = mac.upper()
    mac_windows = []
    mac_windows.append(mac_win[0])
    mac_windows.append(mac_win[1])
    mac_windows.append('-')
    mac_windows.append(mac_win[2])
    mac_windows.append(mac_win[3])
    mac_windows.append('-')
    mac_windows.append(mac_win[5])
    mac_windows.append(mac_win[6])
    mac_windows.append('-')
    mac_windows.append(mac_win[7])
    mac_windows.append(mac_win[8])
    mac_windows.append('-')
    mac_windows.append(mac_win[10])
    mac_windows.append(mac_win[11])
    mac_windows.append('-')
    mac_windows.append(mac_win[12])
    mac_windows.append(mac_win[13])     
    
    print('\nWindows     : ', end='' )
    
    for i in range(0,len(mac_windows)):
        print(mac_windows[i], end='')
    
    ############# HP #############  
    mac_hp_aux = mac.lower()

    #Cria a lista
    mac_hp_aux = list(mac_hp_aux)

    mac_hp_aux[4] = '-'
    mac_hp_aux[9] = '-'

    print('\nHP          : ', end='')

    for i in range(0,len(mac_hp_aux)):
        print(mac_hp_aux[i],end='')

    print(end='\n')
    
    ############# CISCO #############
    print('Cisco       :', mac)


# In[ ]:


##############################################################################################
##############################################################################################
##############################################################################################
sair = ''
while sair != 'S' :
    mac = input('Digitar o endereço MAC: ')

    if mac[2] == '-' and mac[5] == '-' and mac[8] == '-' and  mac[11] == '-' and mac[14] == '-':
        funcao_windows(mac)
    elif mac[2] == ':' and mac[5] == ':' and mac[8] == ':' and  mac[11] == ':' and mac[14] == ':':
        funcao_linux(mac)
    elif mac[4] == '-' and mac[9] == '-':
        funcao_hp(mac)
    elif mac[4] == '.' and mac[9] == '.':
        funcao_cisco(mac)
    else:
        print('formato inválido')
    
    print('\n')
    sair = input('Digite S para sair ou C para continuar: ')
    print('\n')

