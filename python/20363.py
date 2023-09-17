import sys
input=sys.stdin.readline

X, Y = map(int, input().split())
print(int(X + Y + min(X, Y) // 10))