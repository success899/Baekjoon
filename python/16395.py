import sys
input=sys.stdin.readline

n, k = map(int, input().split())
dp = [[1], [1, 1]]

for i in range(2, n):
    tmp = []
    tmp.append(1)

    for j in range(1,i):
        tmp.append(dp[i-1][j-1] + dp[i-1][j])
    tmp.append(1)
    dp.append(tmp)

print(dp[n-1][k-1])