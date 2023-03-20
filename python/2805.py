import sys
input=sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

start, end = 0, max(N_list)

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in N_list:
        if i >= mid:
            tmp += (i - mid)

    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)