import sys
input=sys.stdin.readline

N = int(input())
M = int(input())
room_list = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x, y):
        room_list[i] = 1

result = room_list.count(0)
print(result-1)