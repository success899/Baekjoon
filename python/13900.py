import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
sum_N_list = sum(N_list)
result = 0

for n in N_list:
    sum_N_list -= n
    result += sum_N_list * n

print(result)