n = s = 0
while True:
    n = int(input('\033[1;35mDigite um valor a ser somado \033[31m[999 para parar]: \033[m'))
    if n == 999:
        break
    s += n
print(f'\033[1;34mA soma entre os números vale {s}\033[m')