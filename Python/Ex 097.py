def escreva(msg):
    tam = len(msg) + 6
    print('\033[1;34m~\033[m'*tam)
    print(f'\033[1;33m   {msg}\033[m')
    print('\033[1;34m~\033[m'*tam)


escreva('Nicolas Ramos')