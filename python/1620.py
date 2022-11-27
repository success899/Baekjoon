import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list_int = {}
N_list_name = {}

for i in range(1,N+1):
    tmp = input().strip()
    N_list_int[i] = tmp
    N_list_name[tmp] = i

for _ in range(M):
    tmp = input().strip()
    if tmp.isdigit() == True:
        print(N_list_int[int(tmp)])
    else:
        print(N_list_name[tmp])