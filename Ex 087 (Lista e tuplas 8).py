matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna = 0
mais = menos = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[1;34mDigite um valor para a posição (\033[1;33m{l}, {c}\033[m\033[1;34m):\033[1;34m '))
        if matriz [l][c] %2 ==0:
            soma += matriz[l][c]
        if c == 2:
            coluna += matriz[l][c]
        if l == 1:
            if c == 0:
                mais = menos = matriz[l][c]
        if l == 1:
            if matriz[l][c] > mais:
                mais = matriz[l][c]
            if matriz[l][c] < menos:
                menos = matriz[l][c]
print('\033[1;34m=\033[m'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[1;34m[\033[1;33m{matriz[l][c]:^5}\033[1;34m]\033[m', end='')
    print()
print('\033[1;34m=\033[m'*30)
print(f'\033[1;34mA soma de todos os valores pares digitados é: \033[1;33m[{soma}]\033[m')
print(f'\033[1;34mA soma dos valores da terceira coluna é: \033[1;33m[{coluna}]\033[m')
print(f'\033[1;34mO maior valor da segunda linha é: \033[1;33m[{mais}]\033[1;34m e o menor é: \033[1;33m[{menos}]\033[m')
