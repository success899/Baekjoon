import sys
input=sys.stdin.readline

N, K = map(int, input().split())
routes = list(map(int, input().split()))

tmp = sum(routes)
if tmp < K:
    K -= sum(routes)
    for i in range(N-1, -1, -1):
        K -= routes[i]
        if K < 0:
            print(i+1)
            break

elif tmp >= K:
    for i in range(N):
        K -= routes[i]
        if K < 0:
            print(i+1)
            break