import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
result = []
result.append(1)

for i in range (N-1,0,-1):
    if N > i+N_list[i-1]:
        tmp = result[N - i - N_list[i-1] - 1]
        result.append(tmp + 1)
    else:
        result.append(1)
result.reverse()

for i in result:
     print(i, end=" ")