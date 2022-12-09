import sys
input=sys.stdin.readline

N, M = map(int,input().split())

num_list = []

for _ in range(N):
    num_list.append(list(map(int,input().split())))

num_sum_list = [[0]*(N+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        num_sum_list[i][j] = num_sum_list[i][j-1] + num_sum_list[i-1][j] - num_sum_list[i-1][j-1] + num_list[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    sum = num_sum_list[x2][y2] - num_sum_list[x2][y1-1] -num_sum_list[x1-1][y2] + num_sum_list[x1-1][y1-1]
    print(sum)