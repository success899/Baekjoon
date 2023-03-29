import sys
input=sys.stdin.readline

X = list(str(input().rstrip()))
result = 0

while len(X) != 1:
    tmp = 0
    for i in range(len(X)):
        tmp += int(X[i])

    X = list(str(tmp))
    result += 1

print(result)
if int(X[0]) in [3,6,9]:
    print('YES')
else:
    print('NO')