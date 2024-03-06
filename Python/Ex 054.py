import sys
import datetime
soma = 0
sub = 0
for pessoa in range(1, 8, 1):
    n = int(input(f'\033[34mEm que ano a \033[31m{pessoa}ª\033[m \033[34mpessoa nasceu ?\033[m '))
    x = datetime.date.today().year - n
    if n > 2022 or n <= 1925:
        print('\033[31mPOR FAVOR INSIRA UM ANO VALIDO....\033[m')
        sys.exit()
    if x >= 18:
        soma = soma + 1
    elif x < 18:
        sub = sub + 1
print('='*45)
print('\033[34mAo todo tivemos \033[31m{} \033[34mpessoas maiores de idade.\033[m'.format(soma))
print('\033[34mE tivemos \033[31m{} \033[34mpessoas menores de idade.\033[m'.format(sub))
print('='*45)