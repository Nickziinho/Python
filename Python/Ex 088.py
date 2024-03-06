from random import randint
from time import sleep
lista = list()
lista2 = list()
tot = 1
print('\033[1;34m-\033[m'*40)
print(f'\033[1;33m{"JOGO DA MEGA SENA":^40}\033[m')
print('\033[1;34m-\033[m'*40)
print('\033[1;34mQuantos jogos você quer que eu sorteie ?\033[m')
resposta = int(input('\033[1;32mR:\033[m '))
print(f'\033[1;34m========> SORTEANDO \033[1;33m{resposta} \033[1;34mJOGOS <========\033[m')
while tot <= resposta:
    cont = 0
    while True:
        dados = randint(1, 60)
        if dados not in lista:
            lista.append(dados)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
    tot += 1
for c in range (0, resposta):
    print(f'\033[1;34mJogo {c+1}:\033[1;33m {lista2[c]}\033[m')