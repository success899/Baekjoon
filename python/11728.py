import sys
input=sys.stdin.readline

N, M = map(int,input().split())

A = []
A.append(list(map(int,input().split())))

B = []
B.append(list(map(int,input().split())))

A_sum_B = A + B
result = []

for i in A_sum_B:
    for j in i:
        result.append(j)

result.sort()

for i in result:
    print(i, end=' ')