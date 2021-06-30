print('==== CRIANDO UM MENU DE OPÇÕES ====')
act = 4
while act == 4:
    controle = 0
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    while controle == 0:
        act = int(input('''ESCOLHA UMA OPÇÕES:
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos Numeros
        [5] - Sair do Programa
        Sua escolha é: '''))
        if act == 1:
            print('A soma de {} com {} é de {}.'.format(n1,n2,n1+n2))
            controle = 1
        elif act == 2:
            print('O produto de {} com {} é {}.'.format(n1,n2,n1*n2))
            controle = 1
        elif act ==3:
            if n1>n2:
                print('O maior numero é {}.'.format(n1))
                controle = 1
            elif n1 == n2:
                print('Os numeros são iguais.')
                controle = 1
            else:
                print('O maior numero é {}.'.format(n2))
                controle = 1
        elif act ==4:
            controle = 1
        elif act == 5:
            print('\033[1;31mPROGRAMA ENCERRADO')
            controle = 1
        elif act > 5:
            print('Vamos lá, você tem que escolhe entre as opções.')
            controle = 0
print('\033[1;31mFIM DO PROGRAMA')
