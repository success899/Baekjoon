import sys
input=sys.stdin.readline

mod = int(1e9)+7
n = int(input())
result = n-2
x, y = 1, 1

for _ in range(n-2):
    y, x = (x+y) % mod, y

print(y, result)