pessoas = dict()
lista = list()
continuar = ''
soma = 0
while continuar !=  'N':
    pessoas["Nome"] = str(input('Nome: ')).capitalize()
    pessoas["Sexo"] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoas["Sexo"] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoas["Sexo"] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoas["Idade"] = int(input('Idade: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    soma += pessoas["Idade"]
    lista.append(pessoas.copy())
dividido = soma / len(lista)
print('='*30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'A média de idade é de {dividido:.0f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in lista:
    if p["Sexo"] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
for p in lista:
    if p["Idade"] > dividido:
        print(f'Nome: {p["Nome"]}; Sexo: {p["Sexo"]}; Idade: {p["Idade"]}')
print('<< ENCERRADO >>')
