import sys
input=sys.stdin.readline

N, M = map(int,input().split())
A, B = [], []

for i in range(N):
    A_list = list(map(int,input().split()))
    A.append(A_list)

for i in range(N):
    B_list = list(map(int,input().split()))
    B.append(B_list)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j],end=' ')
    print()