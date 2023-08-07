import sys, itertools
input=sys.stdin.readline

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
tmp, tmp_max = 0, 0

for i in range(N):
    combi = list(itertools.combinations(N_list[i], 3))
    temp = 0

    for j in combi:
        temp = max(temp, sum(j) % 10)

    if temp >= tmp_max:
        tmp = i + 1
        tmp_max = temp

print(tmp)