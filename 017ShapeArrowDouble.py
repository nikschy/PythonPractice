n = 11
m = (n//2)+1

for i in range(1,m+1):
    ck = cj = 0
    for k in range(i-1):
        print(' ',end='')
        ck+=1
    for j in range(i):
        print('*',end='')
        cj+=1
    for a in range(2*(n-(cj+ck))):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for k in range(i-1):
        print(' ',end='')
    print()
for i in reversed(range(1,m)):
    ck = cj = 0
    for k in range(i-1):
        print(' ',end='')
        ck+=1
    for j in range(i):
        print('*',end='')
        cj+=1
    for a in range(2*(n-(cj+ck))):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for k in range(i-1):
        print(' ',end='')
    print()