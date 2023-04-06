import sys
input=sys.stdin.readline

N = int(input())
N_list = []

for _ in range(N):
    N_list.append(float(input()))

N_list.sort()

for i in range(7):
    print(f'{N_list[i]:.3f}')