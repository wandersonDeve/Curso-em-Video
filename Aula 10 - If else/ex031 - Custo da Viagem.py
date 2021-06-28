from time import sleep
print('==== CALCULANDO O VALOR DAS VIAGENS ====')
km = float(input('Digite em KM a distancia da viagem: '))
print('CALCULANDO O VALOR COM BASE NA DISTANCIA ....')
sleep(2)

if km <= 200:
    print('O valor da viagem é de R$ {:.2f}'.format(km*0.50))
else:
    print('O valor da viagem é de R$ {:.2f}'.format(km*0.45))
