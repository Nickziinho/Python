from time import sleep
from random import choice
nome = str(input('Qual é seu nome, eu vou te dizer se tu é gostosa ou não sua biscati: ')).upper().strip()
gostosa = 1
ngostosa = 2
lista = [gostosa, ngostosa]
escolhido = choice(lista)
print('\033[0:33mPROCESSANDO SE VOCÊ É UMA GOSTOSA.....\033[m')
sleep(3)
if escolhido == gostosa:
    print('\033[35mVocê {} \033[0;32mÉ UMA GOSTOSA, \033[1;32mVOU TE MAMAR'.format(nome))
if escolhido == ngostosa:
    print('\033[35mVocê {}, \033[0;31mNÃO É UMA GOSTOSA, \033[1;33mFEDIDA CORNA'.format(nome))
