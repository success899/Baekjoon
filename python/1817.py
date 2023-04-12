import sys
input=sys.stdin.readline

N, M = map(int, input().split())

if N == 0:
    print(0)

else:
    N_list = list(map(int, input().split()))
    tmp = 0
    result = 1

    for i in range(N-1, -1, -1):
        tmp += N_list[i]
        if tmp > M:
            result += 1
            tmp = N_list[i]
    
    print(result)