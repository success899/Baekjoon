import sys
input=sys.stdin.readline

N = int(input())
N_list = []
count = 0

for _ in range(N):
    N_list.append(int(input()))

if N == 1 or N_list[0] > N_list[N_list[1:].index(max(N_list[1:]))+1]:
    print(0)
else:
    while True:
        if N_list[0] > max(N_list[1:]):
            print(count)
            break
        N_list[N_list[1:].index(max(N_list[1:]))+1] -= 1
        N_list[0] += 1
        count += 1