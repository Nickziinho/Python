nome = str(input('Qual seu nome completo? ').strip())
dividir = nome.split()
contar = ''.join(dividir)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(contar)} letras.')
print(f'Seu primeiro nome é {dividir[0]}.')
