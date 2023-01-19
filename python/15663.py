import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.sort()
Num_tmp = []
result = []
tmp = [False] * N

def func():
    if len(Num_tmp) == M:
        temp = ' '.join(map(str, Num_tmp))
        if temp not in result:
            result.append(temp)
        return None

    for i in range(len(N_list)):
        if not tmp[i]:
            tmp[i] = True
            Num_tmp.append(N_list[i])
            func()
            del Num_tmp[-1]
            tmp[i] = False

func()

for i in result:
    print(i)