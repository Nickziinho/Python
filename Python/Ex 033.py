n1 = int(input('\033[0;34mDigite o primeiro valor:\033[m '))
n2 = int(input('\033[0;34mSegundo valor:\033[m '))
n3 = int(input('\033[0;34mTerceiro valor:\033[m '))
#Quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[0;31mO menor número é {}.\033[m'.format(menor))
print('\033[0;32mO maior número é {}.\033[m'.format(maior))