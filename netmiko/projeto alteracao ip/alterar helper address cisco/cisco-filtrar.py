# Importar expressão regular
import re

# Lista conteudotodo arquivo de configuração do switch
lista = []
#
# Contar o número de interfaces que possui as interfaces vlans configuradas
cont_interface = 0

# Lista do resultado final
lista_result = []

lista_result_invalido = []

# Importar o arquivo de backup
with open('config_cisco/arquivo.log', 'r') as tex:
    for linha in tex:
        # Armanzer cada linha do arquivo em uma posição da lista
        lista.append(linha.strip())
tex.close()

# procurar_por: 'interface Vlan-interface'
for i in range(0,len(lista)):
    # Procurar por pela palavra chave
    re_inicio = re.search(r'interface Vlan',lista[i])

    # Sub-lisa contendo o conteúdo procurado
    sub_lista = []

    # Se encontrar a palavra n inicio
    if re_inicio is not None:
        cont_w = i

        # Enquanto não encontrar o final do comando
        while lista[cont_w] != '!':
            sub_lista.append(lista[cont_w])
            # Quantidade de interface Vlans
            cont_w += 1

    contem_80_1 = False
    contem_80_2 = False

    # Sub-lista: corresponde a cada interface vlan
    if len(sub_lista) > 0:
        for j in range(0, len(sub_lista)):
            # r1 = re.search(r'ip helper-address 10.15.80.1',sub_lista[j])
            # if r1 is not None:
            #     contem_80_1 = True

            r2 = re.search(r'ip helper-address 10.15.80.2',sub_lista[j])
            if r2 is not None:
                contem_80_2 = True

        if contem_80_1 or contem_80_2:
            # Contador do número de interface VLANs encontradas.
            cont_interface = cont_interface + 1

            # Espaço entre as interfaces VLANs
##################################################
            # lista_result.append('')
##################################################

            # Escrever a interface VLAN XXXX
            lista_result.append(sub_lista[0])

            # Escrever os comandos
#             if contem_80_1:
#                 lista_result.append('no ip helper-address 10.15.80.1')
#                 lista_result.append('ip helper-address 10.93.80.201')

            if contem_80_2:
                lista_result.append('no ip helper-address 10.15.80.2')
                lista_result.append('ip helper-address 10.92.82.2')

print(f'Foram encontradas {cont_interface} interfaces VLANs.')

# Salvar em disco o arquivo
with open('output_cisco/saida_arquivo.log', 'w') as texto:
    for f in range(0,len(lista_result)):
        texto.write(lista_result[f])
        texto.write('\n')
