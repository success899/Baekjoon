import sys
input = sys.stdin.readline

N, K = map(int,input().split())
N_list = list(map(int,input().split()))

result = [sum(N_list[:K])]

for i in range(1, len(N_list) - K + 1):
    temp = result[-1] + N_list[i+K-1] - N_list[i-1]
    result.append(temp)

print(max(result))