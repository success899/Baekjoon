import sys
input=sys.stdin.readline

T = int(input())
tmp = [True] * 1001

for i in range(2, 40):
    if not tmp[i]:
        continue
    for j in range(2 * i, 1001, i):
        tmp[j] = False

for _ in range(T):
    K = int(input()) - 3
    for i in range(2, 1001):
        if tmp[i] and tmp[K - i]:
            result = [3, i, K - i]
            break
    print(*sorted(result))