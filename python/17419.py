import sys
input=sys.stdin.readline

N = int(input())
K = str(input().rstrip())

result = 0

for i in K:
    if i == '1':
        result += 1

print(result)