print('==== SOMANDO CARACTERES ====')

var = input('DIGITE UMA FRASE: ')
var_up = var.upper().strip()

print("Essa frase aparece {} vezes a letra 'A'."
      "\nEla aparece pela primeira vez na posição {}."
      "\nAparece pela ultima vez na posição {}."
      .format(var_up.count('A'),var_up.find('A')+1,var_up.rfind('A')+1))