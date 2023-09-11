import sys
input=sys.stdin.readline

N = int(input())
tmp = 0
N_list = []
for i in range(N):
    N_list.append(int(input()))  
    tmp += N_list[i] * (-1) ** i
result = tmp // 2

print(result)
for i in range(N-1):
    result = N_list[i] - result
    print(result)