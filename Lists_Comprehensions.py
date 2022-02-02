lista = list(range(1, 10))

print(lista)

pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 != 0]

print(pares)
print(impares)