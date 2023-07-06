import sys
input=sys.stdin.readline

N, M = map(int, input().split())
one, six, result = [], [], 0

for _ in range(M):
    tmp = list(map(int, input().split()))
    one.append(tmp[1])
    six.append(tmp[0])

one, six = min(one), min(six)

if one * 6 <= six:
    result = N * one
else:
    if one * (N%6) <= six:
        result = (six * (N//6)) + ((N%6) * one)
    else:
        result = (six * ((N//6) + 1))

print(result)