import sys
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
 
dp = [[0, 1000000000]]
 
for i in range(1, N+1):
    dp.append([max(dp[i-1][0], A_list[i-1] - dp[i-1][1]), min(dp[i-1][1], A_list[i-1])])
 
for i in range(1, N+1):
    print(dp[i][0], end = ' ')