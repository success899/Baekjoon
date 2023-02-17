import sys
input=sys.stdin.readline

N = int(input())

DP = [0, 1, 1]

for i in range(3, N+1):
    tmp = DP[i-1] + DP[i-2]
    DP.append(tmp)

print(DP[N])