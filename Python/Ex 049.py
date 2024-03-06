n = int(input('\033[34mDigite o numero que deseja ver a tabuada:\033[m '))
for tab in range(1,11):
    print('{} x {} = {}'.format(n, tab, n * tab))