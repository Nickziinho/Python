print('\033[31m=\033[m'*25)
print('\033[1;31m10 TERMOS DE UMA PA\033[m')
print('\033[31m=\033[m'*25)
t = int(input('\033[1;34mPrimeiro termo:\033[m '))
r = int(input('\033[1;34mRazão:\033[m '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print(f'\033[31m{c}\033[m', end='\033[1;31m ⇾ \033[m')
print('\033[31mFIM\033[m')