print('==== SUPER FORMULARIO ====')

maior = homem = mulher = 0

while True:
    print('-'*20)
    age = int(input('Qual sua Idade: '))
    sexo = str(input('Qual seu sexo:\n[M,F]: ')).upper().strip()
    if age > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and age < 20:
        mulher += 1
    cond = str(input('Deseja continuar ? [S/N] ')).upper().strip()
    if cond == 'N':
        break
print('-'*20)
print(f'Existe nesse cadastro {maior} pessoas com mais de 18 anos de idade.\n'
      f'Foram cadastrados {homem} homens. \n'
      f'E temos {mulher} mulheres com menos de 20 anos de idade')