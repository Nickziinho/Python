num = int(input('\033[;34mDigite um número inteiro:\033[m '))
print('''\033[7;40mEscolha uma das bases para conversão:\033[m
\033[;34m[ 1 ]\033[m \033[;33mconverter para\033[m \033[;35mBINÁRIO\033[m
\033[;34m[ 2 ]\033[m \033[;33mconverter para\033[m \033[;35mOCTAL\033[m
\033[;34m[ 3 ]\033[m \033[;33mconverter para\033[m \033[;35mHEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para \033[;35mBINÁRIO\033m é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para \033[:35mOCTAL\033[m é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para \033[0;35mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)))
else:
    print('\033[0;31mOPÇÃO INVALIDA...\033[m')
