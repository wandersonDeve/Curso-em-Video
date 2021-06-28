print('==== \033[1;34mIMC\033[m ====')

peso = float(input('Qual o seu peso em kg? '))
alt = float(input('Qual sua altura em metros? '))
imc = peso/(alt**2)

print('{:.2f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('Você no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você esta com sobre peso.')
elif imc >= 30 and imc <= 40:
    print('Você esta com obesidade')
elif imc > 40:
    print('\033[1;31mCUIDADO!!!\033[m Você esta com obesidade morbida')