num = cont = soma = 0
print('\033[1;34m-=-'*5)
print('    /SOMAS/')
print('\033[1;34m-=-'*5)
while num != 999:
    num = int(input('\033[34mDigite um número \033[33m[999 para parar]:\033[m '))
    soma += num
    cont += 1
print('\033[1;31m~~'*30)
print('\033[1;35mVocê digitou {} números para a soma. E a soma entre eles é de {}.'.format(cont - 1, soma - 999))