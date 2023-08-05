import sys
input=sys.stdin.readline

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

result = 0

for row in paper:
    result += sum(row)
print(result)