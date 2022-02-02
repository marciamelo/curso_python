heroi = {'Goku':90, 'He-man':85, 'Superman': 95, 'Flash':70}
arma = {'Kamiha':90, 'Espada':95, 'Forca': 85, 'Raio':80}
vilao = {'Thanos':180, 'Loki':170, 'Venon':180, 'Caveira':175}

selecHeroi = input('Escolha um herói: ')
selecArma = input('Escolha uma arma: ')
selecVilao = input('Escolha um vilão: ')

poder = heroi.get(selecHeroi) + arma.get(selecArma)

if poder > vilao.get(selecVilao):
    print(f'{selecHeroi} venceu utilizando o(a) {selecArma}')
elif poder == vilao.get(selecVilao):
    print('Empate, ninguém venceu.')
else:
    print(f'{selecVilao} venceu {selecHeroi}')
