def cadastro():
    lista = []
    for i in range(3):
        dicionario = dict(nome = input('Digite o nome: '),
                          sexo = input('Digite o sexo(F/M): '),
                          esporte = input('Digite o esporte: '),
                          idade = input('Digite a idade: ')
        )
        lista.append(dicionario)
    return lista

def aviso():
    print('Não há homens que gostam de natacao na lista')

lista_idade = cadastro()
cont = 0
soma = 0

for i in lista_idade:
    if lista_idade[i]['sexo'] == 'M' and lista_idade[i]['esporte'] == 'natacao':
        count += 1
        soma = soma + lista_idade[i]['idade']
if count == 0:
    aviso()
else:
    media = soma/cont
    print(f'A média de idade de homens que fazem natacao é: {media}')
