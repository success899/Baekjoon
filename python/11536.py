import sys, math
input=sys.stdin.readline

names = []

for _ in range(int(input())):
    names.append(str(input().rstrip()))

if names == sorted(names):
    print('INCREASING')
elif names == sorted(names, reverse=True):
    print('DECREASING')
else:
    print('NEITHER')