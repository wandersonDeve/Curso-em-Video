print('==== ANALISADOR COMPLETO ====')
saldo = 0
idade = 0
nome = ('')
qtn = 0
for dados in range(1,5):
    name = str(input('Qual o seu nome: ')).strip()
    age = int(input('Qual a sua idade: '))
    sexo = int(input('''' Qual o seu sexo:
    [ 1 ] - masculino
    [ 2 ] - feminino
    digite: '''))
    saldo = saldo + age
    if idade < age and sexo == 1:
        idade = age
        nome = name
    elif age < 20 and sexo == 2:
        qtn = qtn+1

print('''Nesse grupo temos:
uma media de idade de {}.
o homem mais velho se chama {}
e temos {} mulheres com menos de 20 anos de idade'''.format(saldo/4,nome,qtn))
