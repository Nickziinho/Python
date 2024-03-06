soma = 0
print('\033[1;31m=\033[m'*25)
print('\033[1;7;35;40mANALISAR NÚMEROS PRIMOS.\033[m')
print('\033[1;31m=\033[m'*25)
num = int(input('\033[34mDigite um número:\033[m '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
    div = num % c
    if div == 0:
        soma = soma + 1
print(f'\n\033[34mO número \033[33m{num}\033[m \033[34mfoi divisível \033[33m{soma}\033[m \033[34mvezes\033[m')
if soma > 2 or soma == 1 or soma == 0:
    print('\033[34mPor isso ele\033[m \033[31mNÃO É PRIMO\033[m.')
else:
    print('\033[34mPor isso ele\033[m \033[32mÉ PRIMO\033[m.')
