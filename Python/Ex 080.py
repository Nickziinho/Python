lista = list()
for c in range(0,5):
    num = (int(input('Digite um valor: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista..')
    else:
        pos = 0
        while pos < len[lista]:
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista..')
                break
            pos += 1
lista.sort()
print(lista)