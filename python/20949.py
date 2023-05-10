import sys, math
input=sys.stdin.readline

N = int(input())
monitors = []

for i in range(N):
    W, H = map(int, input().split())
    PPI = math.sqrt(W ** 2 + H ** 2) / 77

    monitors.append([i+1, PPI])

monitors.sort(key=lambda x: (-x[1], x[0]))

for i in monitors:
    print(i[0])