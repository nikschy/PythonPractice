n = 11
center = n//2
for i in range(center+1):
    for j in range(n):
        if (i<=center) and (center-i<=j<=center+i):
            print('*',end="")
        else:
            print(' ',end="")
    print()

for i in reversed(range(center)):
    for j in range(n):
        if (i<=center) and (center-i<=j<=center+i):
            print('*',end="")
        else:
            print(' ',end="")
    print()