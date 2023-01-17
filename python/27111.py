import sys
input=sys.stdin.readline

N = int(input())
history = {}
result = 0

for _ in range(N):
    a, b = map(int,input().split())

    if a not in history:
        history[a] = b
        if b == 0:
            result += 1
    else:
        if history[a] == b:
            result += 1
        else:
            history[a] = b

for i in history.values():
    if i == 1:
        result += 1

print(result)