def is_leap(ano):
    if (ano%4 == 0) and (ano%100 != 0) or (ano % 400) == 0:
        return 'True'
    else:
        return 'False'

year = int(input("Digite um ano: "))
print(is_leap(year)) #<<< O atributo year é oque ira substituir o ANO definido ali em cima
""""Eu posso usar o parenteses para deixar o código mais visivel aos olhos cada prcedimento
do processo, ou então eu posso deixar apenas sem, não faz diferença nem uma na linha de 
programação, a diferença é apenas visual para não ficar tudo junto e misturado"""
