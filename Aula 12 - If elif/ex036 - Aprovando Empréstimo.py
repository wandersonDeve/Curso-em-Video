from time import sleep
print('==== \033[1;36mAPROVANDO EMPRESTIMO\033[m ====')

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario mensal? '))
mensal = int(input('Em quantos meses você pretende pagar a casa? '))
mensalidade = casa / mensal
controle = salario * 0.3

print('Pagando essa casa no valor de R$ {:.2f} em {} meses, você pagará R$ {:.2f} por mês'.format(casa,mensal,mensalidade))
sleep(5)
print('\033[1;35mVerificando a possibilidade de emprestimo....\033[m')
sleep(3)
if mensalidade >= controle:
    print('\033[1;31mInfelizmente seu emprestimo não foi aprovado.\033[m')
else:
    print('\033[1;33mPARABENS\033[m, seu emprestimo foi aprovado com sucesso.')