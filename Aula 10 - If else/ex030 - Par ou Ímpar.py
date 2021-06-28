print('==== IMPAR OU PAR ====')

num = int(input('Digite um numero inteiro: '))
unidade = num % 2

if unidade == 0:
    print('O numero {} é um numero par'.format(num))
else:
    print('O numero {} é um numero impar'.format(num))
