carro = float(input('Qual é a velocidade atual do carro? '))
if carro >80:
    multa = (carro - 80) * 7
    print(f'MULTADO! você execedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${multa}!')
print('Tenha um bom dia! Dirija com cuidado!')