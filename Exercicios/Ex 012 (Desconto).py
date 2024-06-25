carteira = float(input('Qual é o preço do produto? R$'))
porcentagem = float(input('Quantos % de desconto ele tem? '))
valor = carteira * (porcentagem / 100)
resultado = carteira - valor
print(f'O produto que custava R${carteira}, na promoção com desconte de {porcentagem:.0f}% vai custar R${resultado:.2f}')
