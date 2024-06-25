salario = float(input('\033[0;34mDigite o valor do salario:\033[m \033[0;32mR$\033[m'))
if salario > 1250:
    aumento = salario * (10 / 100 + 1)
    print(f'Quem ganhava \033[0;32mR${salario}\033[m passa a ganhar \033[0;32mR${aumento:.2f}\033[m.')
else:
    aumento15 = salario * (15 / 100 +1)
    print(f'Quem ganhava \033[0;32mR${salario}\033[m passa a ganhar \033[0;32mR${aumento15:.2f}\033[m.')
