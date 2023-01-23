import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.sort()
Num_tmp = []

def func():
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))
        return None

    temp_num = 0

    for i in range(len(N_list)):
        if temp_num != N_list[i]:
            Num_tmp.append(N_list[i])
            temp_num = N_list[i]
            func()
            del Num_tmp[-1]

func()