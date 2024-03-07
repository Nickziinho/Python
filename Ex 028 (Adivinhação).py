from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
computador = randint(0, 5)
pensar = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if pensar == computador:
    print(f'GANHOU,o numero que eu pensei foi {computador}, meus parabén, você acertou.')
else:
    print(f'PERDEU,o número que eu pensei foi {computador}, não foi dessa vez. HAHA')
