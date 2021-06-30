print('==== PROGRESSAO ARITMETICA ====')

i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

pr = i

while pr != r*10+i:
    print('{} ->'.format(pr+r), end=' ')
    pr = pr + r
print('FIM DA PROGRESSAO')