import sys
input=sys.stdin.readline

N, K = map(int, input().split())
count = 0
check_list = [False] * (N+1)

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if check_list[j] != True:
            check_list[j] = True
            count += 1
            if count == K:
                print(j)