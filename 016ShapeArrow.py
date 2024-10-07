n = 21
for i in range(1,(n+1)//2):
    for k in range(i-1):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in reversed(range(1,n//2)):
    for k in range(i-1):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()