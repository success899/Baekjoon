import sys
input=sys.stdin.readline

N = int(input())
count = 0
max_count = 0
for _ in range(N):
    name = str(input().rstrip())
    K, M = map(int, input().split())
    tmp = 0
    while K <= M:
        M -= K
        M += 2
        tmp += 1
    count += tmp
    if tmp > max_count:
        max_count = tmp
        max_name = name

print(count)
print(max_name)