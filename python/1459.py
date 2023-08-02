import sys
input=sys.stdin.readline

X, Y, W, S = map(int, input().split())
result = 0

if 2 * W <= S:
    print((X+Y) * W)
else:
    tmp1 = min(X, Y)
    result = tmp1 * S
    tmp2 = abs(X-Y)
    if W > S:
        if tmp2 % 2 == 0:
            result += tmp2 * S
        else:
            result += (tmp2-1) * S + W
    else:
        result += tmp2 * W
    print(result)