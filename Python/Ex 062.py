print('\033[31m=\033[m'*25)
print('\033[1;31m10 TERMOS DE UMA PA\033[m')
print('\033[31m=\033[m'*25)
primeiro = int(input('\033[1;34mPrimeiro termo:\033[m '))
razao = int(input('\033[1;34mDigite a razão:\033[m '))
termo = primeiro
cont = 1
total = 0
r = 10
while r != 0:
    total += r
    while cont <= total:
        print('{} '.format(termo), end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    r = int(input('Quantos termos você quer mostrar a mais ? (Digite 0 para sair do programa)'))
print(f'Progressão finalizada com {total} termos mostrados.')