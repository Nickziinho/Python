import sys
from datetime import date
n1 = int(input('\033[34mInforme seu ano de nascimento:\033[m '))
n2 = date.today().year - n1
print('='*50)
if n2 <= 9:
    print(f'\033[0;34mVocê possui \033[35m{n2}\033[m \033[34mAnos.\033[m\n\033[34mVocê se enquadra em ser um nadador\033[m \033[0;33mMIRIM\033[m')
elif n2 <= 14:
    print(f'\033[0;34mVocê possui \033[35m{n2}\033[m \033[34mAnos.\033[m\n\033[34mVocê se enquadra em ser um nadador\033[m \033[0;33mINFANTIL\033[m')
elif n2 <= 19:
    print(f'\033[34mVocê possui \033[35m{n2}\033[m \033[34mAnos.\033[m\n\033[34mVocê se enquadra em ser um nadador\033[m \033[33mJÚNIOR\033[m')
elif n2 <= 25:
    print(f'\033[34mVocê possui \033[35m{n2}\033[m \033[34mAnos.\033[m\n\033[34mVocê se enquadra em ser um nadador\033[m \033[33mSÊNIOR\033[m')
else:
    print(f'\033[34mVocê possui \033[35m{n2}\033[m \033[34mAnos.\033[m\n\033[34mVocê se enquadra em ser um nadador\033[m \033[33mMASTER\033[m')
print('='*50)
