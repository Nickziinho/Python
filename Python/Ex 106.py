from time import sleep
cores = ('\033[m',         #0 - sem cor
         '\033[1;31m',     # 1 - vermelho
         '\033[1;34m',     # 2 - azul
         '\033[1;37m',     # 3 - ciano
         '\033[1;32m',     # 4 - verde
         )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    sleep(1)
    print(cores[2], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('\033[1;34mFunção ou biblioteca:\033[m '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 4)