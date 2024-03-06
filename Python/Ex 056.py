count = 0
média = 0
maior = 0
nomevelho = ''
for p in range(1, 5):
    print(f'\033[1;35m----- {p}ª PESSOA -----\033[m')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    média = média + idade
    maiuscula = sexo.upper()
    if maiuscula == 'F' and idade < 20:
        count = count + 1
    if p == 1:
        maior = idade
    else:
        if idade > maior and maiuscula == 'M':
            maior = idade
            nomevelho = nome
div = média / 4
print('\033[34m-=-\033[m'*25)
print(f'\033[33mA média de idade do grupo é de {div}.\033[m')
print(f'\033[33mO homem mais velho do grupo tem {maior} anos e se chama {nomevelho}.\033[m')
print(f'\033[mAo todo são {count} mulheres com menos de 20 anos.\033[m')
print('\033[34m-=-\033[m'*25)