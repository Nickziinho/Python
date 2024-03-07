matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[1;34mDigite um valor para a posição (\033[1;33m{l}, {c}\033[m\033[1;34m):\033[1;34m '))
print('\033[1;34m=\033[m'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[1;34m[\033[1;33m{matriz[l][c]:^5}\033[1;34m]\033[m', end='')
    print()
