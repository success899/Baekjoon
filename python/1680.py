import sys
input=sys.stdin.readline

for _ in range(int(input())):
    W, N = map(int, input().split())
    garbage = [tuple(map(int, input().split())) for _ in range(N)]

    w = x = d = 0
    for x_i, w_i in garbage:
        d += x_i - x
        x = x_i
        w += w_i

        if w > W:
            d += x_i * 2
            w = w_i

        if w == W: 
            d += x_i
            x = 0
            w = 0

    d += x

    print(d)