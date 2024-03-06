from math import sin, cos, tan, radians
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'O valor do seno é {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}.')
