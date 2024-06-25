from random import randint
import sys
soma = 1
print('\033[1;34m-=-\033[m'*20)
print('\033[1;33mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;34m-=-\033[m'*20)
computador = randint(0, 5)
pensar = int(input('\033[1;35mEm que número estou pensando?\033[m '))
if pensar != computador:
    print('\033[1;33mVocê errou eu pensei em {}\033[m'.format(computador))
if pensar == computador:
    print(f'\033[1;34mMeus parabéns você acertou de \033[32mPRIMEIRA\033[m.')
    print('\033[1m=\033[m' * 40)
    sys.exit()
print('\033[1m=\033[m'*30)
while pensar != computador:
    computador = randint(0, 5)
    pensar = int(input('\033[31mTente novamente:\033[m '))
    if pensar != computador:
        print('\033[1;33mVocê errou eu pensei em {}\033[m'.format(computador))
        print('\033[1m=\033[m'*30)
    soma += 1
    if pensar == computador:
        print(f'\033[1;36mMeus parabéns eu pensei em {computador} e você acertou, você teve {soma} tentativas até acertar.\033[m ')
