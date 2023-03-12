import sys
input=sys.stdin.readline

while True:
    tmp = list(map(int, input().split()))
    result = 0
    
    if len(tmp) == 2:
        if tmp[0] == 0 and tmp[1] == 0:
            break
        else:
            N, M = tmp[0], tmp[1]
            N_M_dict = {}
    for _ in range(N):
        num = int(input())
        N_M_dict[num] = 1
    for _ in range(M):
        num = int(input())
        if N_M_dict.get(num) == 1:
            result += 1

    print(result)