import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_sum = sum(N_list)
result = 0

for i in N_list:
    N_sum -= i
    result = (result + i * N_sum) % 1000000007
print(result)