sexo = str(input('\033[34mInforme seu sexo \033[32m[M/F]\033[m\033[34m:\033[m ')).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('\033[31mPor favor informe um sexo válido [M/F]:\033[m ')).upper().strip()[0]
print(f'\033[34mSexo \033[32m{sexo}\033[m \033[34mregistrado com sucesso.\033[m')