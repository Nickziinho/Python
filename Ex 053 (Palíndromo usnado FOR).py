palavra = str(input('Digite uma frase (não considere a acentuação): ')).strip()
upper = palavra.upper()
split = upper.split()
junto = ''.join(split)
inverso = ''
for letra in range(len(junto) -1, -1 ,-1):
    inverso += junto[letra]
print(f'Você digitou a frase \033[33m{junto}\033[m e o inverso dela é \033[33m{inverso}\033[m.')
if junto == inverso:
    print('Essa frase \033[32mÉ UM PALÍNDROMO\033[m.')
else:
    print('Essa frase \033[31mNÃO É UM PALÍNDROMO\033[m.')

#Possivel substituir o for por inverso = junto[0:0:-1]
