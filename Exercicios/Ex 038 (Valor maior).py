n1 = float(input('\033[;33mPrimeiro número: '))
n2 = float(input('Segundo valor:\033[m '))
if n1 > n2:
    print('O \033[1;34mPRIMEIRO\033[m valor é o \033[;32mMAIOR\033[m')
elif n2 > n1:
    print('O \033[1;34mSEGUNDO\033[m valor é o \033[;32mMAIOR\033[m')
else:
    print('Os \033[1;34mDOIS\033[m valores são \033[;32mIGUAIS\033[m')
