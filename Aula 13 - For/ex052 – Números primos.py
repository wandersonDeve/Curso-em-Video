print('==== NUMEROS PRIMOS ====')

print('VALOR VER SE UM NUMERO É PRIMO.')
num = int(input('Digite um numero: '))
soma = 0

for cada in range(1,num+1):
    if num % cada == 0:
        soma = cada+soma

if soma == num+1:
    print('O numero é primo')
else:
    print('Esse numero não é primo')
print('\033[1;31mFIM DO PROGRAMA')
