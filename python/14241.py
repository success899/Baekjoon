import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort(reverse=True)

tmp = 0
result = 0

for i in range(0, N-1):
    tmp = N_list[i] * N_list[i+1]
    N_list[i+1] = N_list[i] + N_list[i+1]
    result = result + tmp

print(result)