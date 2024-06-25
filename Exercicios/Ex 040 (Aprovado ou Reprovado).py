import sys
a = float(input('\033[0;34mDigite a nota da prova A1:\033[m '))
if a > 10:
    print('\033[1;31mPor favor coloque valores até 10 e não mais que isso...\033[m')
    sys.exit()
b = float(input('\033[0;34mDigite a nota da prova A2:\033[m '))
c = (a + b) / 2
if a > 10 or b > 10:
    print('\033[1;31mPor favor coloque valores até 10 e não mais que isso...\033[m')
elif c < 5:
    print('\033[1;34mA média de suas notas são {}.\033[m\n\033[1;31mVocê foi REPROVADO.\033[m'.format(c))
elif c >= 5 and c <= 6.9:
    print('\033[1;34mA média de suas notas são {}.\033[m\n\033[1;33mVocê está de RECUPERAÇÃO.\033[m'.format(c))
else:
    print('\033[1;34mA média de suas notas são {}.\033[m\n\033[1;32mVocê está APROVADO.\033[m'.format(c))
