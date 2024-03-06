import sys
import random
itens = ('\033[1;36mPEDRA\033[m', '\033[1;36mPAPEL\033[m', '\033[1;36mTESOURA\033[m')
computador = random.randint(0, 2)
print('\033[1;31m='*25)
print('\033[1;7;33;40mBORA JOGAR UM JOKENPÔ\033[m\n\033[1;7;33;40m.....SUAS OPÇÕES.....\033[m')
print('\033[1;31m='*25)
print('\033[1;32m[ 0 ]\033[m \033[1;35mPEDRA\033[m')
print('\033[1;32m[ 1 ]\033[m \033[1;35mPAPEL\033[m')
print('\033[1;32m[ 2 ]\033[m \033[1;35mTESOURA\033[m')

jogador = int(input('\033[34mQual você escolhe ?\033[m '))

if jogador > 2:
    print('\033[31mJOGADA INVALIDA, FAÇA DENOVO.\033[m')
    sys.exit()

print('\033[1;m-=-\033[m'*15)
print('\033[1;mO computador escolheu {}\033[m'.format(itens[computador]))
print('\033[1;mO jogador escolheu {}\033[m'.format(itens[jogador]))
print('\033[1;m-=-\033[m'*15)

if computador == 0:                                 #COMPUTADOR ESCOLHE PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE.\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU.\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU.\033[m')
elif computador == 1:                               #COMPUTADOR ESCOLHE PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU.\033[m')
    if jogador == 1:
        print('\033[1;33mEMPATE.\033[m')
    if jogador == 2:
        print('\033[1;32mJOGADOR VENCEU.\033[m')
elif computador == 2:                               #COMPUTADOR ESCOLHE TESOURA
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCEU.\033[m')
    if jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCEU.\033[m')
    if jogador == 2:
        print('\033[1;33mEMPATE.\033[m')
else:
    print('\033[31mJOGADA INVALIDA...\033[m')