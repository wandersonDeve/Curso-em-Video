print('==== SEU NOME ====')
nome = input('Qual seu nome: ')
jun = nome.split()
jun1 = ''.join(jun)

print('Seu nome em Letras Maiusculas é {}'.format(nome.upper()))
print('Seu nome em Letras Maiusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(jun1)))
print('Seu primeiro nome tem {} letras'.format(len(jun[0])))
