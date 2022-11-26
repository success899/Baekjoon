import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list = []
count = 0

for _ in range(N):
    N_list.append(input())

for _ in range(M):
    tmp = input()
    if tmp in N_list:
        count += 1

print(count)