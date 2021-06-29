print('\033[1;33m==== SOMANDO OS NUMEROS IMPARES'
      ' MULTIPLOS DE 3 ====\033[m')
soma = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        soma = soma+impar

print('''A soma dos numeros de 1 até 500 que sao impares e
multiplos de 3 é de {}'''.format(soma))
