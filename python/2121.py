import sys
input=sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
xy_set = set(tuple(map(int, input().split())) for _ in range(N))

count = 0

for i, j in xy_set:
    if ((i+A, j) in xy_set) and ((i, j+B) in xy_set) and ((i+A, j+B) in xy_set):

        count += 1

print(count)