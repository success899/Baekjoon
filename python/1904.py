import sys
input=sys.stdin.readline

N = int(input())
dp = [1, 2]

for i in range(N-2):
    tmp = (dp[i] + dp[i+1]) % 15746
    dp.append(tmp)

print(dp[N-1])