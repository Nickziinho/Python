cont = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print(f'A soma de todos os {cont} valores solicitados é {soma}', end=' ')
