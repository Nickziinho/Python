jogador = {}
gols = list()
dados = list()
soma = 0
jogador["Nome"] = str(input('Nome do jogador: ')).strip().capitalize()
quantidade = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
for g in range(0, quantidade):
    golo = int(input(f'Quantos gols na partida {g+1}? '))
    soma += golo
    gols.append(golo)
jogador["Gols"] = gols
jogador["Total"] = soma
print('\033[1;34m=\033[m'*30)
for i, c in jogador.items():
    print(f'O campo {i} tem o valor {c}')
