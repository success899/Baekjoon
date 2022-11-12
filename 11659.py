import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
result = [0]
temp = 0

for i in N_list:
    temp += i
    result.append(temp)


for _ in range(M):
    i, j = map(int,input().split())
    print(result[j] - result[i-1])