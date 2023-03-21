import sys
input=sys.stdin.readline

K, N = map(int, input().split())
K_list = []
for _ in range(K):
    K_list.append(int(input()))

start, end = 1, max(K_list)

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in K_list:
        tmp += (i//mid)

    if tmp >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)