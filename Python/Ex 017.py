from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digita o valor do cateto adjacente: '))
hi = hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hipotenusa é {hi:.2f}.')