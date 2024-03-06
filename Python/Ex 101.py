def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f'Você tem: {idade} anos seu voto não é \033[1;32mNÃO VOTA.\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem: {idade} anos seu voto é \033[1;33mOPCIONAL.\033[m'
    else:
        return f'Você tem: {idade} anos seu voto é \033[1;31mOBRIGATÓRIO.\033[m'


nasc = (int(input('\033[1;34mDigite o ano do seu nascimento:\033[m ')))
print('\033[1;34m=\033[m'*30)
print(voto(nasc))