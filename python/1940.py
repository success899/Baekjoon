import sys
input=sys.stdin.readline

N = int(input())
M = int(input())
N_list = list(map(int, input().split()))

N_list.sort()
start, end = 0, N-1
count = 0

while start < end:
    N_sum = N_list[start] + N_list[end]

    if N_sum < M:
        start += 1
    elif N_sum > M:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)