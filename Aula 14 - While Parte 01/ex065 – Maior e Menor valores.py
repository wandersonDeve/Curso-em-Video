print('==== MAIOR E MENOR ====')

maior = menor = media = qtn = 0
con = 'S'

while con != 'N':
    a = int(input('Digite um numero: '))
    media += a
    qtn += 1
    if a > maior:
        maior = a
        if menor == 0:
            menor = a
    elif a < menor:
        menor = a
    con = str(input('Deseja continuar a digitar numeros? [ S , N ] ')).upper().strip()
print('O maior numero digitado foi \033[1;35m{}\033[m '
      'e o menor foi \033[1;34m{}\033[m'
      ' com a media de \033[1;36m{:.2f}\033[m.'.format(maior,menor,media/qtn))
print('\033[1;31mFIM DO PROGRAMA')
