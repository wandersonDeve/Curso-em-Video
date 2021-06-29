print('\033[1;34m==== MAIOR E MENOR PESO ====\033[m')

maior = 0
menor = 0

for peso in range(1,6):
    kg = float(input('Informe o peso da pessoa '
                       'numero {}: '.format(peso)))
    if kg > maior:
        maior = kg
        menor = kg
    elif kg < menor:
        menor = kg
print('O peso mais alto foi de {}Kg '
      'e o menor foi de {}Kg'.format(maior,menor))
