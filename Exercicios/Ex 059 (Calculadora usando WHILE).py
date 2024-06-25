import time
r = 1
print('\033[1;33m-=-\033[m'*12)
print('\033[1;34m  / SOMAR / MULTIPLICAR / MAIOR /\033[m')
print('\033[1;33m-=-\033[m'*12)
n1 = int(input('\033[1;34mDigite o primeiro valor:\033[m '))
n2 = int(input('\033[1;34mDigite o segundo valor:\033[m '))
print('\033[1m=\033[m' * 25)
while r == 1 or r == 2 or r == 3:
    print('\033[1;33mOque deseja fazer ?\033[m ')
    print('\033[1;34m[ 1 ] \033[35mSomar\033[m')
    print('\033[1;34m[ 2 ] \033[35mMultiplicar\033[m')
    print('\033[1;34m[ 3 ] \033[35mMaior número\033[m')
    print('\033[1;34m[ 4 ] \033[35mNovos números\033[m')
    print('\033[1;34m[ 5 ] \033[35mSair do programa\033[m')
    print('\033[1m=\033[m'*25)
    r = int(input('\033[1;32mSua resposta:\033[m '))
    while r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
        print('\033[1m=\033[m'*25)
        time.sleep(3)
        print('\033[1;33mOque deseja fazer ?\033[m ')
        print('\033[1;34m[ 1 ] \033[35mSomar\033[m')
        print('\033[1;34m[ 2 ] \033[35mMultiplicar\033[m')
        print('\033[1;34m[ 3 ] \033[35mMaior número\033[m')
        print('\033[1;34m[ 4 ] \033[35mNovos números\033[m')
        print('\033[1;34m[ 5 ] \033[35mSair do programa\033[m')
        print('\033[1m=\033[m' * 25)
        r = int(input('\033[1;32mSua resposta:\033[m '))
    if r == 1:
        soma = n1 + n2
        print('\033[1;34m>>>>>> {} + {} = \033[1;32m{}\033[m'.format(n1, n2, soma))
        print('\033[1m=\033[m' * 25)
        time.sleep(3)
    elif r == 2:
        multi = n1 * n2
        print('\033[1;34m>>>>>> {} * {} = \033[1;32m{}\033[m'.format(n1, n2, multi))
        print('\033[1m=\033[m' * 25)
        time.sleep(3)
    elif r == 3:
        if n1 > n2:
            maior = n1
            print('\033[1;34mEntre {} e {} maior número é:\033[m \033[1;32m{}\033[m'.format(n1, n2, maior))
            print('\033[1m=\033[m' * 25)
            time.sleep(3)
        if n2 > n1:
            maior = n2
            print('\033[1;34mEntre {} e {} maior número é:\033[m \033[1;32m{}\033[m'.format(n1, n2, maior))
            print('\033[1m=\033[m' * 25)
            time.sleep(3)
        if n1 == n2:
            print('\033[1;33mOs dois valores são iguais.\033[m')
            print('\033[1m=\033[m' * 25)
            time.sleep(3)
    elif r == 4:
        while r == 4:
            n1 = int(input('\033[1;34mDigite o primeiro valor:\033[m '))
            n2 = int(input('\033[1;34mDigite o segundo valor:\033[m '))
            print('\033[1m=\033[m' * 25)
            print('\033[1;33mOque deseja fazer ?\033[m ')
            print('\033[1;34m[ 1 ] \033[35mSomar\033[m')
            print('\033[1;34m[ 2 ] \033[35mMultiplicar\033[m')
            print('\033[1;34m[ 3 ] \033[35mMaior número\033[m')
            print('\033[1;34m[ 4 ] \033[35mNovos números\033[m')
            print('\033[1;34m[ 5 ] \033[35mSair do programa\033[m')
            print('\033[1m=\033[m' * 25)
            r = int(input('\033[1;32mSua resposta:\033[m '))
            while r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
                print('\033[1;31mOpção inválida. Tente novamente.\033[m')
                print('\033[1m=\033[m' * 25)
                time.sleep(3)
                print('\033[1;33mOque deseja fazer ?\033[m ')
                print('\033[1;34m[ 1 ] \033[35mSomar\033[m')
                print('\033[1;34m[ 2 ] \033[35mMultiplicar\033[m')
                print('\033[1;34m[ 3 ] \033[35mMaior número\033[m')
                print('\033[1;34m[ 4 ] \033[35mNovos números\033[m')
                print('\033[1;34m[ 5 ] \033[35mSair do programa\033[m')
                print('\033[1m=\033[m' * 25)
                r = int(input('\033[1;32mSua resposta:\033[m '))
            if r == 1:
                soma = n1 + n2
                print('\033[1;34m>>>>>> {} + {} = \033[1;32m{}\033[m'.format(n1, n2, soma))
                print('\033[1m=\033[m' * 25)
                time.sleep(3)
            elif r == 2:
                multi = n1 * n2
                print('\033[1;34m>>>>>> {} * {} = \033[1;32m{}\033[m'.format(n1, n2, multi))
                print('\033[1m=\033[m' * 25)
                time.sleep(3)
            elif r == 3:
                if n1 > n2:
                    maior = n1
                    print('\033[1;34mEntre {} e {} maior número é:\033[m \033[1;32m{}\033[m'.format(n1, n2, maior))
                    print('\033[1m=\033[m' * 25)
                    time.sleep(3)
                if n2 > n1:
                    maior = n2
                    print('\033[1;34mEntre {} e {} maior número é:\033[m \033[1;32m{}\033[m'.format(n1, n2, maior))
                    print('\033[1m=\033[m' * 25)
                    time.sleep(3)
                if n1 == n2:
                    print('\033[1;33mOs dois valores são iguais.\033[m')
                    print('\033[1m=\033[m' * 25)
                    time.sleep(3)
            elif r == 5:
                print('\033[1;33mPROCESSANDO....\033[m')
                time.sleep(3)
                print('\033[1m=\033[m'*25)
                print('\033[1;31mVocê escolheu sair! volte sempre!\033[m')
    elif r == 5:
        print('\033[1;33mPROCESSANDO....\033[m')
        time.sleep(3)
        print('\033[1m=\033[m' * 25)
        print('\033[1;31mVocê escolheu sair! volte sempre!\033[m')
