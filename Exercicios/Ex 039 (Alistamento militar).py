from datetime import date
n1 = int(input('\033[0;34mAno de nascimento:\033[m '))
cal = date.today().year - n1
if cal == 18:
    print(f'\033[0;34mQuem nasceu em {n1} tem {cal} anos em {date.today().year}\033[m')
    print('Você deve se alistar IMEDIATAMENTE!')
elif n1 > date.today().year:
    print('\033[1;31mPor favor insira um ano válido...\033[m')
elif cal > 18:
    frente = cal - 18
    print(f'\033[0;34mQuem nasceu em {n1} tem {cal} anos em {date.today().year}\033[m')
    print(f'\033[0;31mSeu alistamento já passou, você deveria ter se alistado em {date.today().year - frente}.\033[m')
elif cal < 18:
    tras = 18 - cal
    print(f'\033[0;34mQuem nasceu em {n1} tem {cal} anos em {date.today().year}\033[m')
    print(f'\033[0;32mAinda falta {tras} ano(s) para você se alistar.\nSeu alistamento será em {date.today().year + tras}\033[m')
