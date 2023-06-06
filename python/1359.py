import sys, itertools
input=sys.stdin.readline

N, M, K = map(int, input().split())
result = 0
tmp = []
for i in itertools.combinations(range(N), M):
    tmp.append(i)

for i in tmp:
    count = 0
    for j in range(M):
        if i[j] < M:
            count += 1
    if count >= K:
        result += 1

print(result / len(tmp))