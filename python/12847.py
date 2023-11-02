import sys
input=sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

tmp = m
sum_list = sum(t[:tmp])
result = sum_list

for i in range(tmp, n):
    sum_list += t[i] - t[i - tmp]
    result = max(result, sum_list)

print(result)