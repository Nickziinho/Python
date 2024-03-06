aluguel = float(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
preço = aluguel * 60
rodar = km * 0.15
print(f'O total a pagar é de R${preço + rodar}.')
