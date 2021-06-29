print('==== SOMANDO OS NUMEROS PARES ====')

soma = 0
for num in range(1,7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
print('As somas dos numeros pares são {}'.format(soma))
