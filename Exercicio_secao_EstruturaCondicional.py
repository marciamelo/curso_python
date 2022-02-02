"""

1 - Crie um programa que encontre e imprima as raízes de uma equação do segundo grau, utilizando o método de Bhaskara

"""
# 1
# Equação de segundo grau: A * x ** 2 + B * X + C
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

# Encontrando o valor de delta
delta = (b ** 2) - (4 * a * c)

# Encontrando as raízes de x1 e x2
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'As raízes são {x1} e {x2}')