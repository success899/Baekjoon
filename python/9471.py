import sys
input=sys.stdin.readline

P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    answer = 1
    num1, num2 = 1, 2
    while True:
        if num1 % M == 1 and num2 % M == 1:
            break

        answer += 1
        num1, num2 = num2, (num1 + num2) % M

    print(f"{N} {answer}")