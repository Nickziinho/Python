print('\033[31m=\033[m'*25)
print('\033[1;31mSEQUÊNCIA DE FIBONACCI\033[m')
print('\033[31m=\033[m'*25)
cont = 3
t1 = 0
t2 = 1
termo = int(input('Quantos termos você quer vêr ? '))
print('\033[31m~\033[m'*30)
print('{} - {}'.format(t1, t2), end='')
while cont <= termo:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')