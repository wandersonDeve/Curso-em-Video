from random import randint
from time import sleep

print('==== MUTANDO OS RACHADORES ====')
controle = int(80)
speed = randint(30,100)

print('O radar esta lendo a velocidade que o carro passou .... ')
sleep(2)
print('Leitura concluida sua velocidade foi de {}KM/h.'.format(speed))
sleep(1)

if speed <= controle:
    print('Parabens, você esta dentro do limite de velocidade')
else:
    print('Que feio, você esta acima do limite, sera multado...')
    print('Calculando sua multa .....')
    sleep(3)
    print('Sua multa é de R$ {:.2f}'.format((speed-controle)*7))
    