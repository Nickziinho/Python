jogador = dict()
time = list()
partidas = list()
dado = 0
while True:
    jogador.clear()
    partidas.clear()
    jogador["Nome"] = str(input('\033[1;34mNome do jogador:\033[m ')).strip().capitalize()
    quantidade = int(input(f'\033[1;34mQuantas partidas {jogador["Nome"]} jogou ?\033[m '))
    for g in range(0, quantidade):
        partidas.append(int(input(f'\033[1;34mQuantos gols na partida {g+1}?\033[m ')))
    jogador["Quantidade"] = partidas[:]
    jogador["Gols"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('\033[1;33mDeseja continuar? [S/N]:\033[m ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas S ou N.') 
    if resp == 'N':
        break
print('\033[1;34m=\033[m'*50)
print(f'\033[1;33m{"Cod nome":1}{"Gols":^30}{"Total":>}\033[m')
print('\033[1;34m=\033[m'*50)
for k, v in enumerate(time):
    print(f'\033[1;36m{k:>3}\033[m ', end='')
    for d in v.values():
        print(f'\033[1;36m{str(d):<16}\033[m ', end='')
    print()
print('\033[1;34m-\033[m'*50)
while True:
    dado = int(input('\033[1;32mMostrar dados de qual jogador? (999 para parar)\033[m '))
    if dado == 999:
        break
    if dado >= len(time):
        print(f'\033[1;31mERRO! Não existe jogador com código {dado}!\033[m')
    else:
        print(f'\033[1;34m--LEVANTAMENTO DO JOGADOR {time[dado]["Nome"]}:\033[m')
        for i, g in enumerate(time[dado]["Quantidade"]):
            print(f'  \033[1;33mNo jogo {i+1} fez {g} gols.\033[m')
print('\033[1;32m<<< OBRIGADO VOLTE SEMPRE >>>\033[m')
