print('==== É POSSIVEL CRIAR TRIANGULOS COM ESSAS MEDIDAS? ====')
m1 = float(input('Primeira reta: '))
m2 = float(input('Segunda reta: '))
m3 = float(input('Terceira reta: '))

if m1+m2>=m3 and m2+m3>=m1 and m3+m1>=m2:
    print('Com as medidas {}, {} e {}, é possivel fazer um triangulo.'.format(m1,m2,m3))
else:
    print('Infelizmente com as medidas {}, {} e {}, não é possivel fazer um triangulo.'.format(m1,m2,m3))
