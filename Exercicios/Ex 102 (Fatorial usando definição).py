def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ', end='')
        f *= c
    if show:
        print('= ',end='')
    return f


n = int(input('Digite um valor: '))
print(fatorial(n, show=True))
