import sys
input=sys.stdin.readline

N = int(input())
S = [0 for i in range(10)]
point = 1

while N != 0:
    while N % 10 != 9:
        for i in str(N):
            S[int(i)] += point
        N -= 1
    if N < 10:
        for i in range(N + 1):
            S[i] += point
        S[0] -= point
        break
    else:
        for i in range(10):
            S[i] += (N // 10 + 1) * point
    S[0] -= point
    point *= 10
    N //= 10

print(sum(S) % 1234567)