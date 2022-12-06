import sys
input=sys.stdin.readline

N, M = map(int,input().split())
Num_tmp = []

def func(start_num):
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))

    for i in range(start_num, N+1):
        if i not in Num_tmp:
            Num_tmp.append(i)
            func(i+1)
            del Num_tmp[-1]

func(1)