print('==== CALCULO DE FATORAL ====')

f = int(input('Escolha um numero para ver o seu fatoral: '))
print('{}! ='.format(f), end=' ')
mult = 1

for sim in range(f,0,-1):
    mult = mult*sim
    if sim > 1:
        print('{}x'.format(sim), end='')
    else:
        print('{}'.format(sim), end='')
print(' = {} '.format(mult))

print('-='*20)

one = f+1
x = 1
print('{}! ='.format(f), end=' ')
while one > 2:
    one = one-1
    x = x * one
    print('{}x'.format(one), end='')
print('1 = {} '.format(x))