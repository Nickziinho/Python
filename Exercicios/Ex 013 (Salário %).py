salario = float(input('Qual é o salário do funcionário? R$'))
porcentagem = float(input('Quantos % de aumento ele terá? '))
print(f'Um funcionário que ganhava R${salario} com {porcentagem:.0f}% de aumento, passa a receber R${salario * ((porcentagem/100)+1):.2f}.')
