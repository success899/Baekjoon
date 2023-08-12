import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    X = int(''.join(input().split()))
    Y = int(''.join(input().split()))
    clockwise = input().split()
    new_clockwise = clockwise + clockwise[:M - 1]
    result, count = 0, 0

    for i in range(N):
        result = int(''.join(new_clockwise[i:i + M]))
        if X <= result <= Y:
            count += 1
    print(count)