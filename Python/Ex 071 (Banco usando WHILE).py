print('='*30)
print('{:^30}'.format('BANCO DO SEU ZÉ'))
print('='*30)
sacar = int(input('Qual o valor a ser sacado ? R$'))
dep = 50
total = sacar
totalcont = 0
while True:
    if total >= dep:
        total -= dep
        totalcont += 1
    else:
        if totalcont > 0:
            print(f'Total de {totalcont} cédulas de R${dep}.')
        if dep == 50:
            dep = 20
        elif dep == 20:
            dep = 10
        elif dep == 10:
            dep = 1
        totalcont = 0
