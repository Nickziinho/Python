casa = float(input('\033[0;34mValor da casa:\033[m R$'))
salario = float(input('\033[0;34mSalario do comprador:\033[m R$'))
prestação = float(input('\033[0;34mQuantos anos de financiamento?\033[m '))
meses = prestação * 12
resultado = casa / meses
minimo = salario * 0.3
print('Para pagar um casa de \033[0;32mR${:.2f}\033[m em \033[0;35m{:.0f}\033[m Anos a prestação será de \033[0;32mR${:.2f}\033[m'.format(casa, prestação, resultado))
if resultado <= minimo:
    print('Seu emprestimo foi \033[0;32mACEITO\033[m')
else:
    print('Seu emprestimo foi \033[0;31mNEGADO\033[m')
