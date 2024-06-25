impar = list()
par = list()
for n in range(0, 7):
    num = int(input(f'\033[1;34mDigite o \033[1;33m{n+1}o. \033[1;34mnúmero:\033[m '))
    if num %2 == 0:
        par.append(num)
    if num %2 == 1:
        impar.append(num)
impar.sort()
par.sort()
print('\033[1;34m=\033[m'*30)
print(f'\033[1;34mOs números pares digitados foram \033[1;33m{par}.\033[m')
print(f'\033[1;34mOs números ímpares digitados foram \033[1;33m{impar}.\033[m')
