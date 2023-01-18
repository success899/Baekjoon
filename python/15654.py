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

    for i in N_list:
        if i not in Num_tmp:
            Num_tmp.append(i)
            func()
            del Num_tmp[-1]

func()