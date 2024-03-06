cont = homem = mulheres = 0
while True:
    print('\033[1;35m-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('\033[m\033[1;34mIdade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*30)
    if idade > 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    continuar = str(input('\033[m\033[1;33mDeseja continuar? [S/N] \033[m')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Apenas SIM ou NÃO: ')).upper().strip()[0]
    if continuar == 'N':
        print('\033[1;34m-\033[m'*30)
        break
if cont > 1:
    print(f'\033[1;32mExistem {cont} pessoas acima de 18 anos.\033[m')
else:
    print(f'\033[1;32mApenas {cont} pessoa tem mais que 18 anos.\033[m')
if homem > 1 or homem == 0:
    print(f'\033[1;32mForam cadastrados um total de {homem} Homens.\033[m')
else:
    print(f'\033[1;32mFoi cadastrado {homem} homem.\033[m')
if mulheres > 1 or mulheres == 0:
    print(f'\033[1;32mTem {mulheres} mulheres abaixo de 20 anos.\033[m')
else:
    print(f'\033[1;32mExiste {mulheres} mulher abaixo de 20 anos.\033[m')