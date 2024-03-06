valor = list()
continuar = 'S'
while continuar == 'S':
    print('\033[1;34m=\033[m' * 30)
    num = int(input('\033[1;34mDigite um valor:\033[m '))
    if num not in valor:
        valor.append(num)
        print('\033[1;33mValor adicionado..\033[m')
    else:
        print('\033[1;31mEsse valor já foi adicionado.\033[m')
    continuar = str(input('\033[1;32mDeseja continuar? [S/N]:\033[m ')).upper().strip()[0]
    if continuar != 'N' and continuar != 'S':
        while continuar != 'N' and continuar != 'S':
            print('\033[1;34m=\033[m' * 30)
            print('\033[1;31mPor favor apenas Sim ou Não..\033[m')
            continuar = str(input('\033[1;32mDeseja continuar? [S/N]:\033[m ')).upper().strip()[0]
valor.sort()
print(f'\033[1;33mOs valores que você adicionou foram {valor}\033[m')