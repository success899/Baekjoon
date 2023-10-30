import sys
input=sys.stdin.readline

H, W, X, Y = map(int, input().split())

result = []
B_list = []

for _ in range(H + X):
    B_list.append(list(map(int, input().split())))

for i in range(H):
    result.append(B_list[i][:W])

for i in range(H):
    for j in range(W):
        if i + X < H and j + Y < W:
            result[i+X][j+Y] -= result[i][j]

for i in result:
    print(" ".join(map(str, i)))