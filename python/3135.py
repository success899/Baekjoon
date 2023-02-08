import sys
input=sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
N_list = []
tmp = []

for _ in range(N):
    N_list.append(int(input()))

for i in N_list:
    tmp.append(abs(i - B) + 1)
tmp.append(abs(A - B))

print(min(tmp))