import sys
input=sys.stdin.readline
from itertools import accumulate

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

sumlist = [0] + list(accumulate(A_list))
result = 0

for i in range(N):
    if i + K <= N:
        result = max(result, sumlist[i + K] - sumlist[i])
    else:
        result = max(result, sumlist[N] - sumlist[i] + sumlist[(i + K) % N])

print(result)