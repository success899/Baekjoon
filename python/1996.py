import sys
input=sys.stdin.readline

N = int(input())
N_list = []
result = [[0 for j in range(N)] for i in range(N)]
num_list = ['1','2','3','4','5','6','7','8','9']

for _ in range(N):
    N_list.append(list(map(str, input().rstrip())))

for i in range(N):
    for j in range(N):
        if N_list[i][j] in num_list:
            result[i][j] = '*'
            if j-1 >= 0 and result[i][j-1] != '*':
                result[i][j-1] += int(N_list[i][j])
            if i-1 >= 0 and result[i-1][j] != '*':
                result[i-1][j] += int(N_list[i][j])
            if i+1 < N and j-1 >= 0 and result[i+1][j-1] != '*':   
                result[i+1][j-1] += int(N_list[i][j])
            if j+1 < N and i-1 >= 0 and result[i-1][j+1] != '*':
                result[i-1][j+1] += int(N_list[i][j])
            if i-1 >= 0 and j-1 >= 0 and result[i-1][j-1] != '*':
                result[i-1][j-1] += int(N_list[i][j])
            if i+1 < N and result[i+1][j] != '*':
                result[i+1][j] += int(N_list[i][j])
            if j+1 < N and result[i][j+1] != '*':
                result[i][j+1] += int(N_list[i][j])
            if j+1 < N and i+1 < N and result[i+1][j+1] != '*':
                result[i+1][j+1] += int(N_list[i][j])

for i in range(N):
    for j in range(N):
        try:
            if result[i][j] >= 10:
                result[i][j] = 'M'
        except:
            continue

for i in range(N):
    print(*result[i], sep="")