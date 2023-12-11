import sys, itertools
input=sys.stdin.readline

N, S = map(int, input().split())
N_list = list(map(int, input().split()))
count = 0

for i in range(1, N+1):
    comb = itertools.combinations(N_list, i)

    for j in comb:
        if sum(j) == S:
            count += 1

print(count)