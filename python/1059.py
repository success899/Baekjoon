import sys, math
input=sys.stdin.readline

L = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
num_list.sort()

if n in num_list:
    print(0)
else:
    min = 0
    max = 0
    for i in num_list:
        if i < n:     
            min = i
        elif i > n and max == 0:
            max = i
    max -= 1
    min += 1
    print((n-min)*(max-n+1) + (max-n))