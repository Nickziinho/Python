a = float(input('Preço das compras: '))
print('\033[34mFORMAS DE PAGAMENTO\033[m')
print('\033[33m[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão\033[m')
b = int(input('\033[34mQual a opção desejada ?\033[m '))
print('='*25)
if b == 1:
    c = a - a * 0.10
    print(f'\033[34mPagando a vista no dinheiro ou cheque você ganha\033[m \033[35m10%\033[m \033[34mde desconto.\n\033[34mSendo assim o valor a ser pago será de\033[m \033[32mR${c:.2f}\033[m\033[34m.\033[m')
elif b == 2:
    d = a - a * 0.05
    print(f'\033[34mPagando a vista no cartão você ganha\033[m \033[35m5%\033[m \033[34mde desconto.\nSendo assim o valor a ser pago será de\033[m \033[32mR${d:.2f}\033[m\033[34m.\033[m')
elif b == 3:
    print('\033[34mVocê não tem desconto nessa opção de pagamento.\033[m\n\033[34mSendo assim o valor a ser pago será o preço total\033[m \033[32mR${:.2f}\033[m\033[34m.\033[m'.format(a))
else:
    e = a + a * 1.20
    print('\033[34mPagando em 3x ou mais você terá um juros de\033[m \033[91m20%\033[m.\n\033[34mSendo assim o valor a ser pago será de\033[m \033[32mR${:.2f}\033[m\033[34m.\033[m'.format(e))