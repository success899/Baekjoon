import sys
input=sys.stdin.readline

R, C, W = map(int, input().split())
dp = [[1]*i for i in range(1,32)]
result = 0

for i in range(2, 31):
    for j in range(1, len(dp[i])-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for i in range(R-1, R+W-1):
    for j in range((C-1), C+(i-R)+1):
        result += dp[i][j]

print(result)