import sys
input=sys.stdin.readline

N = int(input())
N_list = []
result = 0

for _ in range(N):
    N_list.append(int(input()))
N_list.sort(reverse=True)

for i in range(N):
    tmp = N_list[i] - i
    if tmp > 0:
        result += tmp

print(result)