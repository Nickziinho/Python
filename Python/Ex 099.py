from time import sleep
def maior(*num):
    cont = maior = 0
    print('Analisando os valores digitados...')
    sleep(1)
    for n in num:
        print(f'{n} ', end='')
        sleep(0.2)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informado {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('~~'*15)


print('~~'*15)
maior(1, 5, 4, 3, 8, 9, 7)
maior(8, 10, 20, 45, 5, 8, 9, 30, 15)