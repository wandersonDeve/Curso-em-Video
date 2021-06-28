from time import sleep
print('-='*12)
print('\033[1;32mTIRANDO A MEDIA DO ALUNO\033[m')
print('-='*12)

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('CALCULANDO SUA MEDIA .....')
sleep(3)
print('Sua media foi {}'.format(media))
if media >= 7:
    print('\033[1;36mPARABENS\033[M, Você esta aprovado.')
elif media <= 5:
    print('\033[1;31mINFEZLIMENTE VOCÊ REPROVOU.\033[m')
else:
    print('\033[1;33mVOCÊ ESTA DE RECUPERAÇÃO, NÃO DESANIME\033[m')
