print('==== PALINDROMO ====')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso da frase \033[1;33m{}\033[m é \033[1;35m{}\033[m'.format(junto,inverso))
if inverso == junto:
    print('\033[1;36mTEMOS UM PALINDROMO\033[m')
else:
    print('\033[1;31mNÃO TEMOS UM PALINDROMO\033[m')