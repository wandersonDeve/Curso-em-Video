print('==== VALIDAÇÃO DE DADOS ====')

base = 'm'

while base !='M' and base != 'F':
    base = str(input('Qual seu sexo: [M ou F] ')).strip().upper()
    if base != 'M':
        if base != 'F':
            print('Favor digite uma das opções:')
print('Seu sexo é {}.'.format(base))
print('Fim do programa')
