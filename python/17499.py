import sys
input=sys.stdin.readline

N, Q = map(int,input().split())
A_list = list(map(int,input().split()))
p = 0

for i in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        A_list[(p + query[1] - 1) % N] += query[2]
    elif query[0] == 2:
        p -= query[1]
    else:
        p += query[1]
        
for i in range(p, p + N):
    print(A_list[i % N], end=' ')