print('==== TRATANDO VARIOS VALORES ====')
soma = -999
qtn = -1
n = 0

while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    soma += n
    qtn += 1
print('Você digitou {} numeros e a soma deles é de {}'.format(qtn,soma))
