import sys
input=sys.stdin.readline

K = int(input())
total = []
max_H, max_W = 0, 0
find_max_H, find_max_W = 0, 0

for i in range(6):
    A, B = map(int,input().split())
    if A == 1 or A == 2:
        total.append(B)
        if  max_H < B:
            max_H = B
            find_max_H = i
    else:
        total.append(B)
        if max_W < B:
            max_W = B
            find_max_W = i

box_big = max_H * max_W


total[find_max_H] = 1
total[find_max_H-1] = 1
total[(find_max_H+1)%6] = 1
total[find_max_W] = 1
total[find_max_W-1] = 1
total[(find_max_W+1)%6] = 1

box_small = 1
for i in total:
    if i != 1:
        box_small *= i

print((box_big-box_small)*K)