import sys
input=sys.stdin.readline

P, N = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result = 0

for i in range(N):
    if P >= 200:
        break
    P += N_list[i]
    result += 1

print(result)