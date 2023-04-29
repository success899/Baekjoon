import sys
input=sys.stdin.readline

N = int(input())
juga = list(map(int, input().split()))[::-1]
tmp, result = 0, 0

for i in range(N):
    tmp = max(tmp, juga[i])
    result = max(result, tmp - juga[i])

print(result)