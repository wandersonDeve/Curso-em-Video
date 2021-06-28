print('\33[1;31m==== CORES NO PYTHON ====\33[m')

nome = input('\33[34mQual o seu nome? ')
age = int(input('Qual sua idade? \33[m'))

print('Ola \033[1;30;41m{}\033[m sua idade é de {} anos,'
      ' \33[7;40mvocê é bem jovem.\033[m'.format(nome,age))
