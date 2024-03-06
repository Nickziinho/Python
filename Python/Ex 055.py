print('\033[33m=\033[m'*28)
print('\033[1;33;47mLendo o peso de cada pessoa\033[m')
print('\033[33m=\033[m'*28)
maior = 0
menor = 0
for c in range (1, 6):
    p = float(input(f'\033[34mDigite o peso da {c}ª pessoa:\033[m '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('\033[33m-=-\033[m'*10)
print('\033[34mO maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}\033[m'.format(menor))
print('\033[33m-=-\033[m'*10)