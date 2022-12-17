import sys
input=sys.stdin.readline

A, B = map(int, input().split())

num_list = []

for i in range(1,B+1):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[A-1:B]))