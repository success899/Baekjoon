import sys
input=sys.stdin.readline

N = int(input())
N_list = [0] * 301
for i in range(N):
    N_list[i] = int(input())

dp = [0] * 301
dp[0] = N_list[0]
dp[1] = N_list[0] + N_list[1]
dp[2] = max(N_list[0] + N_list[2], N_list[1] + N_list[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + N_list[i-1] + N_list[i], dp[i-2] + N_list[i])

print(dp[N-1])