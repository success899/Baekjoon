import sys
input=sys.stdin.readline

N = int(input())
N_list = {}

for _ in range(N):
    tmp = int(input())
    if tmp in N_list:
        N_list[tmp] += 1
    else:
        N_list[tmp] = 1

result = sorted(N_list.items(), key = lambda x: (-x[1], x[0]))
print(result[0][0])