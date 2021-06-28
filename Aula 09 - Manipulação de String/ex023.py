print('==== SEPARANDO DIGITOS DE UM  NUMEROS ====')
nu = int(input('Digite um numero de 4 digitos: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10


print(f'Unidade {u}\nDezena  {d}\nCentena {c}\nMilhar  {m}')
