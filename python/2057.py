import sys, math
input=sys.stdin.readline

N = int(input())
check = [ math.factorial(i) for i in range(21) ]

if N == 0:
    print('NO')
else:
    for i in range(20, -1, -1):
        if N >= check[i]:
            N -= check[i]
    
    if N == 0:
        print('YES')
    else:
        print('NO')