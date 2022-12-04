import sys
input=sys.stdin.readline

arr = [[0] * 30 for _ in range(31)]

for i in range(30):
    arr[0][i] = i+1
for i in range(1,30):
    for j in range(i, 30):
        arr[i][j] = arr[i][j-1] + arr[i-1][j-1]

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    print(arr[N-1][M-1])