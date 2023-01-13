import sys
input=sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse=True)
result = 0

for i in N:
    result += int(i)

if result % 3 != 0 or "0" not in N:
    print(-1)
else:
    print(''.join(N))