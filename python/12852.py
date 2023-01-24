import sys
input=sys.stdin.readline

X = int(input())
dp = [0] * (X + 1)
value = [0] * (X + 1)

for i in range(2,X+1):
    dp[i] = dp[i-1] + 1
    value[i] = i-1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = min(dp[i], dp[i//2]+1)
        value[i] = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = min(dp[i], dp[i//3]+1)
        value[i] = i//3

print(dp[X])
print(X, end=' ')

value_num = X
while value[value_num] != 0:
    print(value[value_num], end=' ')
    value_num = value[value_num]