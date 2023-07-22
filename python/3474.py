import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    result = 0
    i = 5
    while i <= N:
        result += N // i
        i *= 5
    print(result)