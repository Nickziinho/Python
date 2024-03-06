while True:
    n = int(input('\033[1;36mDigite um valor para saber a tabuada dele:\033[m '))
    print('\033[1;34m-\033[m'*25)
    if n < 0:
        break
    for c in range (1, 11):
        multi = c * n
        print(f'\033[1;33m{n} x {c} = \033[1;32m{multi}\033[m')
    print('\033[1;34m-\033[m' * 25)
print('\033[1;31mENCERRADO.\033[m')
