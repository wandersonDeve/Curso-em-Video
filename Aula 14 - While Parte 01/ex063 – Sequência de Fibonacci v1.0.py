print('==== Sequência de Fibonacci ====')

n = int(input('Digite a quantidades de numeros: '))
zero = 0
primeiro = 1
controle = 0

print('{} -> {}'.format(zero,primeiro), end=' ')

while controle != n:
    atual = zero + primeiro
    controle += 1
    print('-> {}'.format(atual), end=' ')
    zero = primeiro
    primeiro = atual
print('\nFim do Programa')
