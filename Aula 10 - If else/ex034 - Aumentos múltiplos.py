from time import sleep
print('==== CALCULANDO O AUMENTO ====')
salario = float(input('Qual seu salario atual? '))
print('CALCULANDO O REAJUSTE .... ')
sleep(2)

if salario >= 1250:
    print('Por seu salario ser de R$ {:.2f} o seu salario terá um '
          'aumento de 10% e passará a ser R$ {:.2f}.'.format(salario,salario*1.10))
else:
    print('Por seu salario ser de R$ {:.2f} o seu salario terá um '
          'aumento de 15% e passará a ser R$ {:.2f}.'.format(salario, salario * 1.15))
