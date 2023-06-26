import sys
input=sys.stdin.readline

N, M = map(int, input().split())
N_list = []
result = [0] * N

for _ in range(N):
    N_list.append(sorted(list(map(int, input().split())), reverse=True))

for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(N_list[j][i])
    max_num = max(tmp)

    for j in range(N):      
        if max_num == N_list[j][i]:
            result[j] += 1

max_result = max(result)
for i in range(N):
    if result[i] == max_result:
        print(i+1, end=' ')