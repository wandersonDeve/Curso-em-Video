print('==== MAIOR E MENOR ====')

one = float(input('Digite o primeiro numero: '))
two = float(input('Digite o segundo numero: '))
three = float(input('Digite o terceiro numero: '))

menor = one

if two<one and two<three:
    menor = two
if three<one and three<two:
    menor = three

maior = one

if two>one and two>three:
    maior = two
if three>one and three>two:
    maior = three

print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))