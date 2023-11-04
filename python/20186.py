import sys
input=sys.stdin.readline

N, K = map(int, input().split())
N_list = sorted(list(map(int, input().split())))
result = 0

for i in range(1, K+1):
    result += N_list[-i] - i + 1

print(result)