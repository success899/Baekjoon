import sys
input=sys.stdin.readline

n = int(input())
dp = [1, 1, 2, 5]

if n > 3:
    for i in range(4, n+1):
        tmp = 0
        for j in range(i):
            tmp += dp[j] * dp[i-j-1]
        dp.append(tmp)

print(dp[n])