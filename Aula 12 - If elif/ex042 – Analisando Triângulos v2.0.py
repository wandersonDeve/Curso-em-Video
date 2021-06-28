print('==== ANALISANDO TRIANGULOS ====')

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('Com essas medidas é possivel formar um triangulo ',end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esosceles')
    elif r2 != r1 and r2 != r3 and r3 != r1:
        print('escaleno')
else:
    print('Não é possivel formar triangulos com essas medidas')