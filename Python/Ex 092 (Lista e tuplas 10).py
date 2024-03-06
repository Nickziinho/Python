from datetime import date
dici = {'Nome': '', 'Idade': '', 'CTPS': ''}
nome = str(input('Nome: ')).capitalize()
nascimento = int(input('Ano de nascimento: '))
trabalho = int(input('Carteira de trabalho (0 não tem): '))
if trabalho > 0:
    contratado = int(input('Ano de contratação: '))
    while contratado > date.today().year or contratado < 1960:
        contratado = int(input(f'Não é possivel ser maior que {date.today().year}: '))
    salariado = float(input('Salário: R$'))
dici['Nome'] = nome
dici['Idade'] = date.today().year - nascimento
dici['CTPS'] = trabalho
dici['Contratação'] = contratado
dici['Salário'] = salariado
dici['Aposentadoria'] = (date.today().year - nascimento) + 30
print('\033[1;34m=\033[m'*30)
for i, k in dici.items():
    print(f'{i} tem o valor {k}.')
