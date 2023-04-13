import sys
input=sys.stdin.readline

H, Y = map(int, input().split())
dp = [0] * (Y+1)
dp[0] = H

for i in range(1, Y+1):
    if i>=5:
        dp[i] = max(int(dp[i-1] * 1.05), int(dp[i-3] * 1.2), int(dp[i-5] * 1.35))
    elif i>=3:
        dp[i] = max(int(dp[i-1] * 1.05), int(dp[i-3] * 1.2))
    else:
        dp[i] = int(dp[i-1] * 1.05)

print(int(dp[Y]))