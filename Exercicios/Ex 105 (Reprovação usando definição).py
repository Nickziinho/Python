def notas(*num, sit=False):
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/ len(num)
    if situa == 'S':
        sit = True
    if sit == True:
        if r['média'] <= 6:
            r['situação'] = ('REPROVADO')
        if r['média'] >= 7:
            r['situação'] = ('APROVADO')
    return r


lista = list()
situa = str(input('Deseja saber se está reprovado ou não ? [S/N]: ')).strip().capitalize()[0]
while situa not in 'SN':
    situa = str(input('Por favor apenas sim ou não [S/N]: ')).strip().capitalize()[0]
resp = notas(4.5, 6.7, 8.7, 9.9)
print(resp)



