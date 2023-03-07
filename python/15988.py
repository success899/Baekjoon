import sys
input=sys.stdin.readline

dp = [1,2,4]
tmp = 3

for i in range(int(input())):
    n = int(input())
    while(n > tmp):
        dp.append((dp[tmp-3]+dp[tmp-2]+dp[tmp-1]) % 1000000009)
        tmp+=1
    print(dp[n-1])