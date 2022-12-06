import sys
input=sys.stdin.readline

N, M = map(int,input().split())
Num_tmp = []

def func():
    if len(Num_tmp) == M:
        print(' '.join(map(str, Num_tmp)))

    for i in range(1, N+1):
        if i not in Num_tmp:
            Num_tmp.append(i)
            func()
            del Num_tmp[-1]

func()