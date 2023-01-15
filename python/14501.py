import sys
input=sys.stdin.readline

N = int(input())
days = []

for _ in range(N):
    days.append(list(map(int, input().split())))

dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+days[i][0], N+1):
        if dp[j] < dp[i] + days[i][1]:
            dp[j] = dp[i] + days[i][1]

print(dp[-1])