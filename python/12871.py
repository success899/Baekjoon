import sys
input=sys.stdin.readline

s = str(input().rstrip())
t = str(input().rstrip())

if s*len(t) == t*len(s):
    print(1)
else:
    print(0)