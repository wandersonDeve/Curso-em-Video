print('\033[1;33mMAIOR IDADE\033[m')
from datetime import date
maior = 0
menor = 0
for ano in range(1,8):
    nas = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(ano)))
    if date.today().year-nas >= 21:
        maior = maior+1
    else:
        menor = menor+1
print('{} pessoas sao maiores de idade,'
      '\n{} pessoas ainda são menores de idade.'.format(maior,menor))
