from random import randint
print('==== jogo da adivinhação ====')

pc = randint(0,10)
ten = 1

print('Ola humano, vou pensar em um numero tente adivinhar.')

player = int(input('O numero que pensei entre 0 e 10 foi: '))

while player != pc:
    player = int(input('Você errou tente novamente: '))
    ten += 1
print('\033[1;35mPARABENS HUMANO\033[m, Você acertou !!!'
      '\nMas precisou de {} tentativas'.format(ten))