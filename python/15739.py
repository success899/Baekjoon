import sys
input=sys.stdin.readline

N = int(input())
target = int(N * (N*N + 1) / 2)
result = True
tmp = []
N_list = []
for i in range(N):
    N_list.append(list(map(int, input().split())))
    tmp.extend(N_list[i])

if N*N == len(set(tmp)) and max(tmp) <= N*N:
    for i in range(N):
        tmp_sum1, tmp_sum2 = 0, 0
        tmp_sum3, tmp_sum4 = 0, 0
        for j in range(N):
            tmp_sum1 += N_list[i][j]
            tmp_sum2 += N_list[j][i]
            tmp_sum3 += N_list[j][j]
            tmp_sum4 += N_list[j][N-j-1]

        if tmp_sum1 != target or tmp_sum2 != target or tmp_sum3 != target or tmp_sum4 != target:
            result = False
            
else:
    result = False

if result:
    print('TRUE')
else:
    print('FALSE')