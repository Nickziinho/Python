cont = 0
num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 está na posição {num.index(3)+1}')
else:
    print('Não existe número 3 digitado.')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n %2 == 0:
        print(n, end=' ')
