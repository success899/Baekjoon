import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    pig = sum(list(map(int, input().split())))
    day = 1
    while N >= pig:
        day += 1
        pig *= 4
    print(day)