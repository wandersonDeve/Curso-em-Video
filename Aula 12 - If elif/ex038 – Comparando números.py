print('==== \033[1;36mCOMPARANDO NUMEROS\033[m ====')

one = float(input('Digite o primeiro numero: '))
two = float(input('Digite o segundo numero: '))
maior = 'Não existe valor maior, pois os dois sao iguais.'
if one > two:
    print('O numero {} é maior que o numero {}'.format(one,two))
elif two > one:
    print('O numero {} é maior que o numero {}'.format(two,one))
else:
    print(maior)
