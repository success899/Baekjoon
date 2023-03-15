import sys
input=sys.stdin.readline

N, M = map(int, input().split())
price, result = 0, 0

P = []
for _ in range(M):
    P.append(int(input()))
P.sort()

for i in range(M):
    egg = min(M-i, N)

    if result < P[i] * egg:
        result = P[i] * egg
        price = P[i]

print(price, result)