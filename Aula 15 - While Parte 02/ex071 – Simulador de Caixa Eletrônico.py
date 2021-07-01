print('==== Banco ====')

valor = int(input('Qual valor você deseja sacar? R$ '))

lobo = valor // 200
peixe = (valor % 200)//100
onca = ((valor%200)%100)//50
mico = (((valor%200)%100)%50)//20
arara = ((((valor%200)%100)%50)%20)//10

if lobo != 0:
    print(f'Total de {lobo} cedulas de R$ 200,00')
if peixe != 0:
    print(f'Total de {peixe} cedulas de R$ 100,00')
if onca != 0:
    print(f'Total de {onca} cedulas de R$ 50,00')
if mico != 0:
    print(f'Total de {mico} cedulas de R$ 20,00')
if arara != 0:
    print(f'Total de {arara} cedulas de R$ 10,00')

# ---------------------------------------------------

