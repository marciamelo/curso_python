valor = int(input('Digite o valor final: '))
fib_list = []
atual = 0
soma = 1
qtde = 0

while qtde < valor:
  fib_list.append(atual)
  atual = atual + soma
  soma = atual - soma
  qtde += 1

print(*fib_list, sep = ' ')

