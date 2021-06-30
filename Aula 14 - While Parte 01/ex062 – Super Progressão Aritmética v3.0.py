print('==== SUPER PROGRESSAO ====')

i = int(input('Digite um numero para iniciar a progressao: '))
r = int(input('Digite a razão: '))
a = 10
pa = i

while pa != r*a+i:
    print('{}'.format(pa), end='->')
    pa += r
    if pa == r*a+i:
        e = int(input('\nQuantos numeros mais: '))
        a += e
        if e == 0:
            print('\033[1;31m FIM DO PROGRAMA')
