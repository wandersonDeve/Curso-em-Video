print('==== PA ====')

i = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razao: '))

for cada in range(i,r*10+i,r):
    print(cada, end='->')
print('FIM')
