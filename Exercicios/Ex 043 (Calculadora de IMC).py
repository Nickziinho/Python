print('='*25)
print('\033[34mCalcule seu IMC.\033[m')
print('='*25)
a = float(input('Informe sua altura (metro e cm): '))
b = float(input('Informe seu peso(kg): '))
c = b / (a * a)
print(f'IMC: {c:.2f}')
if c < 18.5:
    print('Você está \033[1;32mABAIXO\033[m do peso.')
elif c <= 25:
    print('Você está no peso \033[1;32mIDEAL.\033[m')
elif c <= 30:
    print('Você está \033[1;33mSOBREPESO.\033[m')
elif c <= 40:
    print('Você está \033[31mOBESO.\033[m')
else:
    print('Você está em \033[1;91mOBESIDADE MÓRBIDA\033[m, vá se tratar.')
print('='*25)
