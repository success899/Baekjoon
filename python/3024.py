import sys
input=sys.stdin.readline

N = int(input())
N_list = [input() for _ in range(N)]

if N < 3:
    print('ongoing')
    exit()

for i in range(N - 2):
    for j in range(N - 2):
        if N_list[i][j] != '.':
            if N_list[i][j] == N_list[i + 1][j + 1] == N_list[i + 2][j + 2]:
                print(N_list[i][j])
                exit()

for i in range(N - 2):
    for j in range(N - 2):
        if N_list[i][N - j - 1] != '.':
            if N_list[i][N - j - 1] == N_list[i + 1][N - (j + 1) - 1] == N_list[i + 2][N - (j + 2) - 1]:
                print(N_list[i][N - j - 1])
                exit()

for i in range(N - 2):
    for j in range(N):
        if N_list[i][j] != '.':
            if N_list[i][j] == N_list[i + 1][j] == N_list[i + 2][j]:
                print(N_list[i][j])
                exit()

for i in range(N):
    for j in range(N - 2):
        if N_list[i][j] != '.':
            if N_list[i][j] == N_list[i][j + 1] == N_list[i][j + 2]:
                print(N_list[i][j])
                exit()

print('ongoing')