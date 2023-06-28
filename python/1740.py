import sys
input=sys.stdin.readline

N = int(input())
tmp = list(bin(N)[2:])[::-1]
t, result = 1, 0

for a in tmp:
    result += int(a) * t
    t = t * 3
print(result)