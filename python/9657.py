import sys
input=sys.stdin.readline

N = int(input())

dp = [0, 1, 0, 1, 1]

if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if 0 in [dp[i-1],dp[i-3],dp[i-4]]:
            dp.append(1)
        else:
            dp.append(0)

if dp[N]:
    print('SK')
else:
    print('CY')