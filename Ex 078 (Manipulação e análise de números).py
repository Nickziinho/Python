valores = list()
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'\033[1;34mDigite um valor para a posição {v}:\033[m ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('\033[1;36m=\033[m' * 40)
print(f'\033[1;34mVocê digitou os valores:\033[m \033[1;35m{valores}\033[m')
print(f'\033[1;34mO maior valor digitado foi:\033[m \033[1;31m{maior}\033[m\033[1;34m, Na posição: \033[m', end='')
for i, e in enumerate(valores):
    if e == maior:
        print(f'\033[1;31m{i}..\033[m ',end='')
print()
print(f'\033[1;34mO menor valor digitado foi:\033[m \033[1;31m{menor}\033[m\033[1;34m, Na posição: \033[m', end='')
for i, e in enumerate(valores):
    if e == menor:
        print(f'\033[1;31m{i}..\033[m ',end='')
print()
