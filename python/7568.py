import sys
input=sys.stdin.readline

N = int(input())
N_list = []

for _ in range(N):
    x, y = input().split()
    N_list.append([x, y])

for i in N_list:
    result = 1
    for j in N_list:
        if i[0] < j[0] and i[1] < j[1]:
                result += 1
    print(result,end=" ")