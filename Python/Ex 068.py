from random import randint
computador = randint(1, 10)
par = impar = derrota = ''
cont = 0
print('\033[1;34m=-=\033[m'*10)
print('  \033[1;33mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[1;34m=-=\033[m'*10)
while True:
    par = impar = derrota = ''
    escolha = str(input('\033[1;35mPar ou Ímpar? [P/I]:\033[m ')).strip().upper()[0]
    while escolha != 'P' and escolha != 'I':
        escolha = str(input('\033[1;31mAPENAS PAR OU ÍMPAR [P/I]:\033[m ')).strip().upper()[0]
    player = int(input('\033[1;35mEscolha a quantidade de dedos que deseja jogar [0, 10]\033[m: '))
    while player > 10 or player < 0:
        player = int(input('\033[1;31mAPENAS DE 0 A 10:\033[m '))
    soma = computador + player
    if soma % 2 == 0:
        par = 'P'
        print(f'\033[1;34mVocê jogou \033[1;32m{player} \033[1;34me o computador \033[1;32m{computador}\033[1;34m. O total deu \033[1;32m{soma} \033[1;34me isso é \033[1;33mPAR\033[m')
    else:
        impar = 'I'
        print(f'\033[1;34mVocê jogou \033[1;32m{player} \033[1;34me o computador \033[1;32m{computador}\033[1;34m. O total deu \033[1;32m{soma} \033[1;34me isso é \033[1;33mÍMPAR\033[m')
    if escolha == par:
        cont += 1
        print('\033[1;32mVocê VÊNCEU !\033[m')
    elif escolha == impar:
        cont += 1
        print('\033[1;32mVocê VÊNCEU !\033[m')
    else:
        derrota = 'Você PERDEU !'
        print('\033[1;31mVocê PERDEU !\033[m')
    if derrota == 'Você PERDEU !':
        print('\033[1;34m=\033[m' * 25)
        break
    print('\033[1;34m=\033[m'*25)
if cont > 1 or cont == 0:
    print(f'\033[1;33mGAME OVER! \033[1;34mVocê venceu \033[1;33m{cont} \033[1;34mVezes.\033[m')
else:
    print(f'\033[1;33mGAME OVER! \033[1;34mVocê venceu \033[1;33m{cont} \033[1;34mVez.\033[m')
