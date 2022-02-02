carrinho = []
precos = []
total = 0

for item in range(5):
    carrinho.append(input('Digite o nome do produto: '))
    precos.append(float(input('Digite o valor do produto: ')))

print(f'Os itens do seu carrinho são: {carrinho}')

#forma 1:
# print(f'O valor total do seu carrinho é: {sum(precos)}.')

# forma 2:
for item in (precos):
    total += item
print(f'O valor total do seu carrinho é: R${total}.')