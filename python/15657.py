import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.sort()
Num_tmp = []

def func(start_index):
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))
        return None

    for i in range(start_index ,len(N_list)):
        Num_tmp.append(N_list[i])
        func(i)
        del Num_tmp[-1]

func(0)