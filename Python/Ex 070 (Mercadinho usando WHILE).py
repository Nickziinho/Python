custototal = totmil = menor = cont = 0
barato = ''
print('='*30)
print('     LOJA SUPER BARATÃO')
print('='*30)
while True:
    produto = str(input('Nome do produto: '))
    custo = float(input('Preço: $'))
    continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    custototal += custo
    cont += 1
    if custo > 1000:
        totmil += 1
    if cont == 1 or custo < menor:
       menor = custo
       barato = produto
    while continuar not in 'SN':
        continuar = str(input('Por favor, apenas SIM ou NÃO: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\033[1;34m-----------FIM DO PROGRAMA-----------\033[m')
print(f'O total da compra foi {custototal:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor}.')
