print('==== GERENCIADOR DE PAGAMENTOS ====')

valor = float(input('Preço do produto: '))
forma = int(input('Forma de pagamento: '
                  '\n1 - À Vista dinheiro'
                  '\n2 - À Vista cartão'
                  '\n3 - 2x no cartão.'
                  '\n4 - 3x ou mais no cartão.'
                  '\n'))
if forma == 1:
    print('Você escolheu pagar \033[33mà vista no dinheiro\033[m e ganhou 10% de desconto no produto.'
          '\n assim o produto que custava R$ {:.2f} agora passa a custar R$ {:.2f}'.format(valor,valor*0.9))
elif forma == 2:
    print('Você escolheu pagar \033[33mà vista no cartão\033[m assim ganhou 5% de desconto'
          '\no produto que custava R$ {:.2f} passa a custar agora R$ {:.2f}'.format(valor,valor*0.95))
elif forma == 3:
    print('Você escolheu pagar em \033[33m2x no cartão\033[m assim o valor do produto permanece o mesmo.')
elif forma == 4:
    print('Você escolheu pagar em \033[33m3x ou mais no cartao\033[m assim o valor do produto'
          '\nsofrerá um aumento de 20% saindo de R$ {:.2f} e passando a custar R$ {:.2f}'.format(valor,valor*1.2))
else:
    print('Essa opção é inexistente')
