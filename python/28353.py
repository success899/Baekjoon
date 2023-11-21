import sys
input=sys.stdin.readline

N, K = map(int, input().split())
W_list = list(map(int, input().split()))
tmp1, tmp2 = 0, N - 1

W_list.sort()
result = 0

while tmp1 < tmp2:
    if W_list[tmp1] + W_list[tmp2] <= K:
        tmp1 += 1
        tmp2 -= 1
        result += 1
    else:
        tmp2 -= 1
    
print(result)