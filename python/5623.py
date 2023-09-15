import sys
input=sys.stdin.readline

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]

if N == 2:
    print(1, 1)

else:
    result = [(N_list[0][1] + N_list[0][2]-N_list[1][2])//2]
    for i in range(1, N):
        result.append(N_list[0][i] - result[0])
    print(*result)