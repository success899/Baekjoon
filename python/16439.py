import sys, itertools
input=sys.stdin.readline

N, M = map(int, input().split())
like_list = [list(map(int, input().split())) for _ in range(N)]
result = 0

for a, b, c in itertools.combinations(range(M), 3):
    tmp = 0
    for i in range(N):
        tmp += max(like_list[i][a], like_list[i][b], like_list[i][c])
    result = max(result, tmp)

print(result)