lista = []
valor = int(input())

for i in range( 1, valor+1):
    if i%2 == 0:
        lista.append(i)
print(*lista, sep='\n')