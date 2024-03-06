from datetime import date
ano = int(input('\033[0;34mInsira o ano que deseja saber se é bissexto, digite 0 se quiser saber do ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1m=\033[m'*25)
    print(f'O ano {ano} é \033[0;32mBISSEXTO\033[m')
    print('\033[1m=\033[m'*25)
else:
    print('\033[1m=\033[m'*25)
    print(f'O ano {ano} \033[0;31mNÃO é BISSEXTO\033[m')
    print('\033[1m=\033[m'*25)