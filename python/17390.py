import sys
input=sys.stdin.readline

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.sort()

for i in range(1, len(A_list)):
    A_list[i] = A_list[i] + A_list[i-1]
    
for _ in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        print(A_list[R-1])
    else:
        print(A_list[R-1] - A_list[L-2])