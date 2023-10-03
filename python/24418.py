import sys, math
input=sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(5)]

print(math.factorial(2 * n) // (math.factorial(n) ** 2), n ** 2)