import sys
input=sys.stdin.readline

for _ in range(int(input())):
    dp = [1,1,1]
    N = int(input())

    for i in range(3, N+1):
        tmp = dp[i-3] + dp[i-2]
        dp.append(tmp)

    print(dp[N-1])