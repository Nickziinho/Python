lista = list()
cont = 0
while True:
    num = lista.append(int(input('\033[1;34mDigite um valor:\033[m ')))
    cont += 1
    pergunta = str(input('\033[1;33mDeseja continuar ? [S/N]:\033[m ')).strip().upper()[0]
    while pergunta != 'S' and pergunta != 'N':
            pergunta = str(input('\033[1;31mPor favor apenas Sim Ou Não:\033[m ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('\033[1;34m=\033[m' * 30)
if cont > 1:
    print(f'\033[1;32mVocê digitou {cont} Elementos.')
else:
    print(f'\033[1;32mVocê digitou {cont} Elemento.\033[m')
lista.sort(reverse=True)
print(f'Os valores em ordem decescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')