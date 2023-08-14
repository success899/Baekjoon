import sys
input=sys.stdin.readline

A = int(input())
T = int(input())
X = int(input())

bundegi = []
bun = degi = 1
n = 0

while True:
    prev_n = bun
    n += 1
    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(n+1):
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(n+1):
        bundegi.append((degi, 1))
        degi += 1
    if prev_n < T <= bun:
        print(bundegi.index((T, X)) % A)
        break