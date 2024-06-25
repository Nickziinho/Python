from time import sleep
def linhas():
    print('~'*30)
def contador(i , f, p):
    print(f'Contagem de {i} até {f} pulando de {p} em {p}.')
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont} ',end='')
            cont += p
            sleep(0.2)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            cont -= p
            sleep(0.2)
        print('FIM!')


linhas()
contador(1, 10, 1)
linhas()
contador(20, 30, 1)
linhas()
contador(40, 0, 2)
linhas()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
