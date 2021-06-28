
print('==== \033[1;33mCONVERSOR DE BASES NUMERICAS\033[m ====')

num = int(input('Digite um numero inteiro: '))
base = int(input('Agora, escolha a base de conversao:'
                 '\n\033[1;34m1 - Para binario'
                 '\n2 - Para Octal'
                 '\n3 - para Hexadecimal\033[m'
                 '\nEscolha: '))
if base == 1:
    print(' O binario de \033[1;31m{}\033[m é \033[1;31m{}\033[m'.format(num,bin(num)[2:]))
elif base == 2:
    print('O Octal de \033[1;31m{}\033[m é \033[1;31m{}\033[m'.format(num,oct(num)[2:]))
elif base == 3:
    print('O Hexadecimal de \033[1;31m{}\033[m é \033[1:31m{}\033[m'.format(num,hex(num)[2:]))
else:
    print('Boa tentativa ..... ja vi que vc não sabe brincar ..... se é assim ..... terminei por aqui.')