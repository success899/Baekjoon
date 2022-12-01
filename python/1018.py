import sys
input=sys.stdin.readline

N, M = map(int,input().split())

board = []
result = []

for _ in range(N):
    board.append(input())
    
for a in range(N-7):
    for b in range(M-7):
        white_start = 0
        black_start = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 'W', 'B' 각각에 대해 검사
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        white_start += 1
                    else:
                        black_start += 1
                else:
                    if board[i][j] != 'W':
                        black_start += 1
                    else:
                        white_start += 1
        result.append(white_start)
        result.append(black_start)

print(min(result))