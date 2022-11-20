N = int(input())
base = [[0 for _ in range(1,101)] for _ in range(1,101)]
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            base[i][j] = 1

for i in range(100):
    for y in range(100):
        if base[i][y] == 1:
            result += 1
            
print(result)