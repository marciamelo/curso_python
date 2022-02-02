def classParcial(pri, seg, ter, **outros):
    op = input('Houve trapaça? s/n: ')




print('corredores: ')
print('Mercurio (MC) Papa_leguas (PL), Sonic (SN), Flash (FS), Ligeirinho (LG) e SuperHomem (SH)')

pri = input('Vencedor: ')
seg = input('Segundo: ')
ter = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('Ultimo: ')

outros  = {'4':qua, '5':qui, '6':ult}
classParcial(pri, seg, ter, **outros)