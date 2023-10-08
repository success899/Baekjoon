import sys
input=sys.stdin.readline

n, m, t = map(int, input().split())

coke = t
result = 0

for i in range((t // n), -1, -1):
    a = i
    for j in range((t // m), -1, -1):
        b = j
        tmp = (n * a) + (m * b)

        if (t - tmp) < coke and (t - tmp) >= 0:
            result = a + b
            coke = t - tmp

        elif (t - tmp) == coke:
            if a+b > result:
                result = a + b
                coke = (t - tmp)

print(result, coke)