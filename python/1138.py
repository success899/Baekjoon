import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
result = [0] * N

for p in range(1, N+1):
    t = N_list[p-1]
    count = 0
    for i in range(N):
        if count == t and result[i] == 0:
            result[i] = p
            break
        elif result[i] == 0:
            count += 1

print(*result)