km = float(input('Quantos km deu sua viagem? '))
if km <= 200:
    cal = km * 0.50
    print(f'O preço da sua viagem será de R${cal:.2f}.')
else:
    cal2 = km * 0.45
    print(f'O preço da sua viagem será de R${cal2:.2f}.')