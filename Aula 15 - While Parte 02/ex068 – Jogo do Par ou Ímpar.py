from random import randint
print('==== par ou impar ====\n\n')
print('Vamos jogar par ou impar:')

win = soma = 0
while True:
    pc = randint(1,11)
    jogador = int(input('Escolha um numero: '))
    var = int(input('Agora escolha:\n[ 1 ] - par\n[ 2 ] - impar\n'))
    soma = jogador+pc
    print(f'Jogador {jogador} + maquina {pc} = {soma}\n')
    if var == 1:
        if soma % 2 == 0:
            print('\033[1;34mParabens você ganhou um ponto\033[m')
            print('-'*20)
            win += 1
        else:
            print('\033[1;31m Você perdeu\033[m')
            break
    elif var == 2:
        if soma % 2 == 1:
            print('\033[1;34mParabens você ganhou um ponto\033[m')
            print('-' * 20)
            win += 1
        else:
            print('\033[1;31m Você perdeu\033[m')
            break
print('\n')
print('=-'*20)
print(f'Você ganhou um total de {win} vezes.')
print('=-'*20)