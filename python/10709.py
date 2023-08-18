import sys
input=sys.stdin.readline

H, W = map(int, input().split())
sky = []
for _ in range(H):
    sky.append(input())
result = [[0] * W for _ in range(H)]
 
for i in range(H):
    count = 1
    cloud = False
    for j in range(W):
        if not cloud and sky[i][j] == '.':
            result[i][j] = -1
        elif sky[i][j] == 'c':
            cloud = True
            result[i][j] = 0
            count = 1
        elif cloud and sky[i][j] == '.':
            result[i][j] = count
            count += 1
 
for i in result:
    print(*i, end=' ')
    print()