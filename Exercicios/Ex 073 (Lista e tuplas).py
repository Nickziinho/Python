times = ('Palmeiras', 'Atlético-MG', 'Corinthians', 'Coritiba', 'São Paulo', 'Atlético-PR', 'Botafogo', 'Flamengo', 'Santos',
         'América-MG', 'Fluminense', 'Internacional', 'Avaí', 'Bragantino', 'Ceará SC', 'Goiás', 'Cuiabá', 'Atlético-GO',
         'Juventude', 'Fortaleza')
print(f'\033[1;35mLista de times: {times}\033[m')
print('\033[1;34m=\033[m'*30)
print(f'\033[1;35mOs 5 primeiros são: {times[0:5]}\033[m')
print('\033[1;34m=\033[m'*30)
print(f'\033[1;35mOs 4 ultimos são: {times[16:20]}\033[m')
print('\033[1;34m=\033[m'*30)
print('\033[1;35mEm ordem alfabética:\033[m ', end='')
print(sorted(times))
