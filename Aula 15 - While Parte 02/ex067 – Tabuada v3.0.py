print('==== TABUADA 3.0 ====\n')

print('VAMOS FAZER UMA TABUADA\n')
while True:
    print('-*' * 10)
    num = int(input('Digite um numero inteiro: '))
    if num >= 0:
        for n in range(1,11):
            print(f'{n} x {num} = {n*num}')
    else:
        break
print('-='*10)
print('FIM DO PROGRAMA')
print('-='*10)