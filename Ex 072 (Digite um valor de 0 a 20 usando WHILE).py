num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito','Dezenove','Vinte')
digita = int(input('\033[1;35mDigiteu um valor entre 0 e 20:\033[m '))
while digita < 0 or digita > 20:
    digita = int(input('\033[1;31mValor invalido, apenas 0 a 20:\033[m '))
for cont in range(digita, digita+1):
    print(f'\033[1;34mVocê digitou o número {num[cont]}.\033[m')
