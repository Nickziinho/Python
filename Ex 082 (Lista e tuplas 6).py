lista = list()
pares = list()
ímpares = list()
while True:
    num = int(input('\033[1;34mDigite um valor:\033[m '))
    lista.append(num)
    pergunta = str(input('\033[1;33mDeseja continuar? [S/N]:\033[m ')).strip().upper()[0]
    if pergunta == 'N':
        print('\033[1;34m=\033[m' * 30)
        break
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('\033[1;31mPor favor apenas Sim ou Não:\033[m '))
    if num %2 == 0:
        pares.append(num)
    elif num %2 == 1:
        ímpares.append(num)
lista.sort()
print(f'\033[1;34mOs valores digitados foram \033[1;32m{lista}\033[m\033[1;34m.\033[m')
print(f'\033[1;34mOs valores pares foram \033[1;32m{pares}\033[m\033[1;34m.\033[m')
print(f'\033[1;34mOs valores ímpares foram \033[1;32m{ímpares}\033[m\033[1;34m.\033[m')
