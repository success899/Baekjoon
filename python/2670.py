import sys
input=sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(float(input()))

for i in range(1, N):
    N_list[i] = max(N_list[i], N_list[i]*N_list[i-1])

print(f'{max(N_list):.3f}')