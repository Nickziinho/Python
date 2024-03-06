print('\033[0;35m=\033[m'*25)
print('\033[1;34mANALISAR TRIANGULOS.\033[m')
print('\033[0;35m=\033[m'*25)
a = float(input('\033[0;34mDigite o primeiro segmento:\033[m '))
b = float(input('\033[0;34mDigite o segundo segmento:\033[m '))
c = float(input('\033[0;34mDigite o terceiro segmento:\033[m '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos \033[1;32mPODEM FORMAR\033[m um triângulo!', end=' ')
    if a == b == c:
        print('\033[1;32mEQUILATERO!\033[m')
    if a != b != c != a:
        print('\033[1;32mESCALENO!\033[m')
    if a == b != c or b == c != a or a == c != b:
        print('\033[1;32mISÓCELES!\033[m')
else:
    print('Os segmentos \033[1;31mNÃO PODEM FORMAR\033[m um triângulo!')
