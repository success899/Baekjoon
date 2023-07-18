import sys
input=sys.stdin.readline

tmp = [0 for _ in range(1500000)]
n = int(input())
tmp[0:1] = [0, 1]

if n < 0:
    for i in range(-1, n - 1, -1):
        data = tmp[i+2] - tmp[i+1]
        if data < 0:
            tmp[i] = (abs(data) % 1000000000) * -1
        else:
            tmp[i] = data % 1000000000
    if tmp[n] < 0:
        print(-1)
        print(tmp[n] * -1)
    else:
        print(1)
        print(tmp[n])


elif n > 0:
    for i in range(2, n + 1):
        tmp[i] = (tmp[i - 1] + tmp[i - 2]) % 1000000000

    print(1)
    print(tmp[n])

else:
    print(0)
    print(0)