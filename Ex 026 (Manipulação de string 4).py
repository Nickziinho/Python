nome = str(input('Digite uma frase: '))
upper = nome.lower()
minuscula = upper.replace('á','a').replace('â','a')
print('A letra A aparece {} vezes.'.format(minuscula.count('a')))
print('A primeira vez que a letra A aparece é na posição {} '.format(minuscula.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(minuscula.rfind('a')+1))
