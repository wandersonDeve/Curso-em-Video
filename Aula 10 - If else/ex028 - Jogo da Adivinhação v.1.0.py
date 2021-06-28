import random
import time
print('==== PENSANDO EM UM NUMERO ====')

num = random.randint(0,5)
print(num)
choice = int(input('Qual numero entre 0 e 5 a maquina pensou ? '))
print('PROCESSANDO RESPOSTA ...')
time.sleep(2)

if choice == num:
    print('Parabens, de fato pensei no numero {}.'.format(choice))
else:
    print('Infelizmente você perdeu, não pensei no numero {} e sim no numero {}.'
          'mais sorte da proxima vez'.format(choice,num))
