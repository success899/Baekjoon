import sys
input=sys.stdin.readline

N = int(input()) - 1
tmp = 1

for i in range(N, 1, -2):
    tmp = tmp * i

print(tmp % (1000000000 + 7))