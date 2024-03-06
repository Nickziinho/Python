info = dict()
info['Nome'] = str(input('Nome: ')).capitalize()
info['Média'] = float(input(f'Média de {info["Nome"]}: '))
print('='*30)
for n, m in info.items():
    print(f'{n} é igual a {m}')
if info['Média'] < 5:
    print('O resultado é reprovado.')
elif info['Média'] < 6:
    print('O resultado é recuperação.')
else:
    print('O resultado é aprovado.')
