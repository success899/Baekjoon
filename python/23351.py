import sys
input=sys.stdin.readline

N, K, A, B = map(int, input().split())
nepeta  = list(K for _ in range(N))
day = 0

while min(nepeta) != 0:

    for _ in range(A):
        nepeta[nepeta.index(min(nepeta))] += B

    for i in range(N):
        nepeta[i] -= 1

    day += 1

print(day)