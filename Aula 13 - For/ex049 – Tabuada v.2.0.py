print('==== TABUADA SIMPLIFICADA ====')

num = int(input('Digite qual numero você quer ver a tabuada: '))
print('-='*5)
for cada in range(1,11):
    print('{} x {:2} = {}'.format(num,cada,(num * cada)))
print('-='*5)
