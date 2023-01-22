import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.sort()
tmp = [False] * N
Num_tmp = []

def func(start_index):
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))
        return None

    temp_num = 0

    for i in range(start_index, len(N_list)):
        if not tmp[i] and temp_num != N_list[i]:
            tmp[i] = True
            Num_tmp.append(N_list[i])
            temp_num = N_list[i]
            func(i + 1)
            tmp[i] = False
            del Num_tmp[-1]

func(0)