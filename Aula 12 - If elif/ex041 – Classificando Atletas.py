from datetime import date
print('\033[1;34m==== CLASSIFICANDO ATLETAS ====\033[m')

nas = int(input('Em que ano você nasceu? '))
year = date.today().year
ano = year-nas

print('Você tem {} anos e por isso '.format(ano))
if ano <=9:
    print('Você é um atleta MIRIM')
elif ano <= 14:
    print('Você é um atleta INFATIL')
elif ano <=19:
    print('Você é um atleta JUNIOR')
elif ano <= 25:
    print('Você é um atleta SENIOR')
else:
    print('Você é um atleta MASTER')