import sys
input=sys.stdin.readline

n, d = map(int, input().split())
result = 0

for i in range(1, n+1):
    tmp = str(i)

    for j in range(len(tmp)):
        if d == int(tmp[j]):
            result += 1

print(result)