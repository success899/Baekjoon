import sys
input=sys.stdin.readline

N = int(input())

dp = [4, 6]

for i in range(2, N+1):
    tmp = dp[i-2] + dp[i-1]
    dp.append(tmp)

print(dp[N-1])