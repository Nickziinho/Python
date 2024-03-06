from time import sleep
soma = 0
for c in range(1, 7):
    n = int(input('\033[34mDigite o \033[1;35m{}\033[m \033[34mvalor:\033[m '.format(c)))
    if n % 2 == 0:
        soma = soma + n
print('\033[1;32mSerá somado os valores pares aguarde....\033[m')
sleep(2)
print('\033[1;34mA soma dos valores pares é: \033[1;32m{}\033[m'.format(soma))
