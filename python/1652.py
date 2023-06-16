import sys
input=sys.stdin.readline

N = int(input())
room = []
width, length = 0, 0
count = 0
for i in range(N):
    room.append(list(input()))
for i in range(N):
    count = 0
    for j in range(N):
        if room[i][j] == '.':
            count += 1
        else:
            count = 0
        if count == 2:
            width += 1
for i in range(N):
    count = 0
    for j in range(N):
        if room[j][i] == '.':
            count += 1
        else:
            count = 0
        if count == 2:
            length += 1
print(width, length)