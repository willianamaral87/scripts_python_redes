import os

# Import threading
import threading

arq = open("lista_devices.txt")
#arq = open("lista_telefones.txt")
linhas = arq.readlines()


ping_ok = []
ping_nao_ok = []
ping_erro_dns = []

def myping(host):
    response = os.system("ping -i 0.3 -c 3 " + host)

    #print('codigo: ' + str(response))

    if response == 0:
        ping_ok.append(host)
    elif response == 256:
        ping_nao_ok.append(host)
    else:
        ping_erro_dns.append(host)


# Lista de Threads
thread_list = []

for linha in linhas:
    t = threading.Thread(target=myping(linha))
    #print(myping(linha))
    
    thread_list.append(t)
    
    # from the main-thread, starts child threads
for thread in thread_list:
    thread.start()

    # main-thread 'sleeping' in join-method, waiting for child-thread to finish 
for thread in thread_list:
    thread.join()

print('#########################################################')
print('#########################################################')
print('###################### ICMP OK ##########################')
print('#########################################################')
for i in ping_ok:
    print(i.rstrip('\n'))
print('#########################################################')
print('##################### ICMP SEM RESPOSTA## ###############')
print('#########################################################')
for i in ping_nao_ok:
    print(i.rstrip('\n'))
print('#########################################################')
print('#################### ERRO DNS ###########################')
print('#########################################################')
for i in ping_erro_dns:
    print(i.rstrip('\n'))
print('#########################################################')
print('#########################################################')


