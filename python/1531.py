import sys
input=sys.stdin.readline

N, M = map(int, input().split())
board = [[0 for _ in range(100)] for _ in range(100)]
result = 0

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i - 1][j - 1] += 1

for i in range(100):
    for j in range(100):
        if board[i][j] > M:
            result += 1

print(result)