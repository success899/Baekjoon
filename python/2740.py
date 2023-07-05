import sys
input=sys.stdin.readline

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

result = []
for _ in range(N):
    result.append([0] * K)

for i in range(N):
    for j in range(K):
        e = 0
        for k in range(M):
            e += A[i][k] * B[k][j]
        result[i][j] = e

for r in result:
    print(*r)