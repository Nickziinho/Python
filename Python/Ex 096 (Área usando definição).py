def Area(l, c):
    s = l * c
    print(f'A área de um terreno {largura}x{comprimento} é de {s}m².')



print('Controle de Terrenos')
print('--'*15)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
Area(largura, comprimento)
