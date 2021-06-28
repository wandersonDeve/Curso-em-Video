from datetime import date
print('==== \033[1;33mALISTAMENTO MILITAR\033[m  ====')

ano = int(input('Em que ano você nasceu ? '))
hoje = date.today().year
soma = hoje-ano

if soma < 18:
    print('Falta {} anos para poder se alistar no serviço militar'.format(18-soma))
elif soma > 18:
    print('Faz {} anos que você deveria ter se alistado e por esse motivo deve regularizar sua situação.'.format(soma-18))
elif soma == 18:
    print('Esse é o ano em que vc completa 18 anos e pode se alistar agora mesmo.')
