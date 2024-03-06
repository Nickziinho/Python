import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Qaurto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'Os alunos escolhidos foram {lista}')