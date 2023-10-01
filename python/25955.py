import sys
input=sys.stdin.readline

N = int(input())
N_list = input().split()
level = ['B','S','G','P','D']
N_list2, result = [0] * N, []

for i in range(N):
    N_list2[i] = level.index(N_list[i][0]) * 1000 + (1000 - int(N_list[i][1:]))

if N_list2 == sorted(N_list2):
    print('OK')
else:
    print('KO')
    for i in range(N):
        if N_list2[i] != sorted(N_list2)[i]:
            result.append(N_list[i])
    print(' '.join(reversed(result)))