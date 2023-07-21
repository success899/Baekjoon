import sys
input=sys.stdin.readline

N = int(input())
N_list = []
result = 0

for _ in range(N):
    N_list.append(int(input()))
N_list.sort(reverse=True)

for i in range(len(N_list)-2):
    if N_list[i] < N_list[i+1] + N_list[i+2]:
        result = N_list[i] + N_list[i+1] + N_list[i+2]
        break
    else:
        result =- 1

print(result)