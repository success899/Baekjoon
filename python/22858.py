import sys
input=sys.stdin.readline

N, K = map(int, input().split())
S_list = list(map(int, input().split()))
D_list = list(map(int, input().split()))

for _ in range(K):
    tmp = [0] * N
    
    for i in range(N):
        tmp[D_list[i]-1] = S_list[i]
    S_list = tmp

print(*S_list)