import random
print('-='*8)
print('\033[1;34mJOGANDO JOKEPÔ\033[m')
print('-='*8)

var = random.randint(1,3)
player = int(input('VALOR JOGAR, ESCOLHA:'
                   '\n1 - Pedra'
                   '\n2 - Papel'
                   '\n3 - Tesoura'
                   '\n'))

if player == 1 and var == 3:
    print('Você ganhou afinal Pedra ganha de tesoura')
elif player == 1 and var == 2:
    print('Você PERDEU, pedra perde para o papel.')
elif player == 1 and var == 1:
    print('EMPATE, tambem escolhi Pedra')
elif player == 2 and var == 1:
    print('Você Ganhou afinal Papel ganha de Pedra')
elif player == 2 and var == 2:
    print('EMPATE, tambem escolhi papel')
elif player == 2 and var == 3:
    print('Você PERDEU, papel perde para o tesoura.')
elif player == 3 and var == 1:
    print('Você PERDEU, tesoura perde para o pedra.')
elif player == 3 and var == 2:
    print('Você ganhou afinal tesoura ganha de papel')
elif player == 3 and var == 3:
    print('EMPATE, tambem escolhi tesoura')
else:
    print('Tentando dar uma de esperto neh.... sendo assim nao brinco mais.')