animais = ['cachorro', 'cavalo', 'baleia', 'gato', 'urso', 'carneiro', 'cabra', 'cobra', 'coelho','mosquito', 'peixe', 'macaco']

listab = [item for item in animais if len(item) <= 7 and item[0] == 'c']

print(listab)