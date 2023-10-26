import sys
input=sys.stdin.readline

N, M = map(int, input().split())
N_list = [input().split() for _ in range(N)]
N_list.sort(key=lambda x: int(x[1]))

M_list = [int(input()) for _ in range(M)]

for char in M_list:
    right = len(N_list)
    left = 0
    result = 0
    while left <= right:
        mid = (left+right) // 2
        if int(N_list[mid][1]) >= char:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(N_list[result][0])