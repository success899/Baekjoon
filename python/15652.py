import sys
input=sys.stdin.readline

N, M = map(int,input().split())
Num_tmp = []

def func(start_num):
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))
        return None

    for i in range(start_num, N+1):
        Num_tmp.append(i)
        func(i)
        del Num_tmp[-1]

func(1)