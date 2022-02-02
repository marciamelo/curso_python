'''
#1) Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário
numero = int(input('Digite um nro inteiro: '))
soma = 0

for cont in range(1, numero+1):
    if numero % cont == 0:
        soma = soma + cont
        print(cont)
print(soma)
'''

#2) Faça um programa que imprima os n primeiros multiplos de 5, sendo n definido pelo usuário
numero = int(input('Digite um nro: '))

for cont in range(1,numero+1):
    print(cont*5)
