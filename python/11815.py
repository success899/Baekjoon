import sys
input=sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

for i in range(N):
    if X[i] == int(X[i] ** 0.5) ** 2:
        print(1, end=" ")
    else:
        print(0, end=" ")