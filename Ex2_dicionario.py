flores = {'Rosas Vermelhas':145, 'Girassóis':125, 'Margaridas':120, 'Flores do campo':140}
presentes = {'Urso de Pelúcia':55, 'Caixa de Bombom':60,'Colar':75, 'Roupas':40}
lugares = {'Praia':70, 'Sair para jantar':150, 'Parque de diversões':120, 'Hotel':180}

flor_cara = ''
flor_valor = 0

presente_caro = ''
presente_valor = 0

lugar_caro = ''
lugar_valor = 0

valor_total = 0

for flor, valor1 in flores.items():
    if valor1 > flor_valor:
        flor_cara = flor
        flor_valor = valor1
valor_total += flor_valor

for presente, valor2 in presentes.items():
    if valor2 > presente_valor:
        presente_caro = presente
        presente_valor = valor2
valor_total += presente_valor

for lugar, valor3 in lugares.items():
    if valor3 > lugar_valor:
        lugar_caro = lugar
        lugar_valor = valor3
valor_total += lugar_valor


print(flor_cara, flor_valor)
print(presente_caro, presente_valor)
print(lugar_caro, lugar_valor)
print(valor_total)



