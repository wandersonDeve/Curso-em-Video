print('==== SERA QUE O ANO É BISSEXTO ? ====')

ano = int(input('Digite um ano que deseja verificar se é bissexto: '))

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano é BISSEXTO.')
else:
    print('O ano não é BISSEXTO.')
