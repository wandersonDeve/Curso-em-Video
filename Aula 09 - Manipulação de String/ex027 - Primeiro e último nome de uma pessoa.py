print('==== NOME E SOBRENOME ====')

nome = input('QUAL SEU NOME: ')
sep = nome.strip().split()

print(f"Primeiro = {sep[0]}\nSegundo  = {sep[len(sep)-1]}")