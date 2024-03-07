from time import sleep
nota = list()
nota2 = list()
nome = list()
média = list()
cont = 0
while True:
    ndado = str(input('\033[1;34mNome:\033[m ')).capitalize()
    nome.append(ndado)
    for n in range(0, 2):
        dados = float(input(f'\033[1;34mNota {n+1}:\033[m '))
        nota.append(dados)
    nota2.append(nota[:])
    nota.clear()
    cont += 1
    continuar = str(input('\033[1;34mDeseja continuar? [S/N]:\033[m ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\033[1;34m=\033[m'*40)
print(f'\033[1;35m{"No.":<4}{"NOME":<10}{"MÉDIA":>8}\033[m')
print('\033[1;34m=\033[m'*40)
for p in range(0, cont):
    print(f'\033[1;33m{p+1:<4}{nome[p]:<10}{(nota2[p][0]+nota2[p][1])/2:>8}\033[m')
print('\033[1;34m=\033[m'*40)
while True:
    pergunta = int(input('\033[1;34mDeseja mostrar a nota de qual aluno ? \033[1;32m(99 Interrompe)\033[m\033[1;34m:\033[m '))
    if pergunta == 99:
        print('\033[1;32m-\033[m' * 40)
        break
    while pergunta > cont:
        pergunta = int(input(f'\033[1;31mPor favor numero maximo é {cont}:\033[m '))
    print('\033[1;32m-\033[m'*40)
    print(f'\033[1;34mNota de \033[1;33m{nome[pergunta-1]} \033[1;34msão: \033[1;33m{nota2[pergunta-1]}\033[m')
    print('\033[1;32m-\033[m'*40)
print('\033[1;35mFINALIZANDO....\033[m')
sleep(2)
print('\033[1;32m<<< VOLTE SEMPRE >>>\033[m')
