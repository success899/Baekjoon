import sys
input=sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(list(map(int, input().split())))
N_list.sort(key= lambda x : (x[0],x[1]))
result = -1

for i in range(N):
    if N_list[i][0] >= result:
        result = N_list[i][0] + N_list[i][1]
    else:
        result += N_list[i][1]

print(result)