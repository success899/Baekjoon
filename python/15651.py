import sys
input=sys.stdin.readline

N, M = map(int,input().split())
Num_tmp = []

def func():
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))
        return None

    for i in range(1, N+1):
        Num_tmp.append(i)
        func()
        del Num_tmp[-1]

func()