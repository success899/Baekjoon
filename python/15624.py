import sys
input=sys.stdin.readline

n = int(input())
a, b = 0, 1

for i in range(n):
    a, b = b%1000000007, (a+b)%1000000007

print(a)