lista_geral = []

lista_geral.append(0)
lista_geral.append(1)
    
for i in range(2, 61):
    lista_geral.append( lista_geral[i-2] + lista_geral[i-1] )

t = int(input())

for cont in range(t):
    N = int(input())
    print("Fib(%d) = %.f" % (N, lista_geral[N]))
