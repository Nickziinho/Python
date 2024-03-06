def ficha(jogador='<Desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gols no campeonato.')


nome = str(input('Nome do jogdador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
