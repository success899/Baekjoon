import sys
input=sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
start, end, count = 0, 0, 0

while end <= N:
    A_sum = sum(A[start:end])
    if A_sum < M:
        end += 1
    elif A_sum > M:
        start += 1
    elif A_sum == M:
        count += 1
        end += 1

print(count)