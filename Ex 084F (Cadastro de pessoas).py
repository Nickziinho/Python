lista =  list()
dados = list()
maispeso = menospeso = 0
while True:
    dados.append(str(input('\033[1;34mNome:\033[m ')))
    dados.append(float(input('\033[1;34mPeso:\033[m ')))
    if len(lista) == 0:
        maispeso = menospeso = dados[1]
    else:
        if dados[1] > maispeso:
            maispeso = dados[1]
        if dados[1] < menospeso:
            menospeso = dados[1]
    lista.append(dados[:])
    dados.clear()
    pergunta = str(input('\033[1;34mDeseja continuar? [S/N]:\033[m ')).upper().strip()[0]
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('\033[1;31mPor favor apenas, Sim ou Não:\033[m ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('\033[1;31m=\033[m'*40)
if len(lista) == 1:
    print(f'\033[1;34mFoi cadastrado \033[1;33m{len(lista)}\033[m \033[1;34mpessoa.\033[m')
else:
    print(f'\033[1;34mForam cadastradas \033[1;33m{len(lista)}\033[m \033[1;34mpessoas.\033[m')
print(f'\033[1;34mO maior peso foi de \033[1;33m{maispeso}\033[m\033[1;34mKg. Peso de:\033[m ', end='')
for p in lista:
    if p[1] == maispeso:
        print(f'\033[1;32m{p[0].capitalize()}\033[m ', end='')
print()
print(f'\033[1;34mO menor peso foi de \033[1;33m{menospeso}\033[m\033[1;34mKg. Peso de:\033[m ', end='')
for p in lista:
    if p[1] == menospeso:
        print(f'\033[1;32m{p[0].capitalize()}\033[m ', end='')
print()
