from gettext import find


rows = 9
cols = 9
board = [[0 for j in range(cols)] for i in range(rows)]

for i in range(9):
    temp = list(map(int,input().split()))

    for y in range(9):
        board[i][y] = temp[y]

max_value = max(map(max, board))

for i in range(9):
    for y in range(9):
        if board[i][y] == max_value:
            row = i+1
            col = y+1

print(max_value)
print(row,col)