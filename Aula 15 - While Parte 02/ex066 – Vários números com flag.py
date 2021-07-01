print('==== WHILE STOP ====')

num = print('Digite 999 para parar o programa')

soma = qtn = 0

while True:
    num = int(input('Digite um numero inteiro qualquer: '))
    if num == 999:
        break
    soma += num
    qtn += 1

print(f'Foram digitados {qtn} e a soma deles é de {soma}')
