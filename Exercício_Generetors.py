listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha',
'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

lista1 = (item for item in listaAnimais if len(item) > 5 and (item[0] == 'C' or item[0] == 'A'))
lista2 = list(lista1)

for item2 in lista2:
    print(item2, end = ' ')
