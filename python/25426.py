import sys
input=sys.stdin.readline

N = int(input())
N_list = []

for _ in range(N):
    a, b = map(int, input().split())
    N_list.append([a, b])
N_list.sort()
result = 0

for i in range(N):
    result += (N_list[i][0] * (i+1) + N_list[i][1])
print(result)