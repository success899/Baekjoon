import sys
input=sys.stdin.readline

N, K = map(int, sys.stdin.readline().split())
baguni = K * (K + 1) // 2

if N < baguni:
    print(-1)
else:
    if (N - baguni) % K == 0:
        print(K - 1)
    else:
        print(K)