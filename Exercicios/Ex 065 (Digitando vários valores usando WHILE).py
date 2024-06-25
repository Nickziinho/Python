r = ''
cont = soma = 0
while r != 'N':
    num = int(input('\033[1;34mDigite um número:\033[m '))
    r = str(input('\033[1;33mQuer continuar ? [S/N]: ')).upper().strip()[0]
    print('\033[1;31m~\033[m'*25)
    cont += 1
    soma += num
    média = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while r != 'S' and r != 'N':
        r = str(input('\033[1;31mINVÁLIDO. \033[1;33mApenas Sim ou Não: ')).upper().strip()[0]
        print('\033[1;31m~\033[m' * 25)
print('\033[1;32mVocê digitou {} números e a média deles foi {}\033[m'.format(cont, média))
print('\033[1;32mO maior valor foi {} e o menor foi {}\033[m'.format(maior, menor))
