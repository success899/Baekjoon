import sys, heapq
input=sys.stdin.readline

N = int(input())
lesson_list = []
for _ in range(N):
    S, T = map(int, input().split())
    lesson_list.append([S, T])

lesson_list.sort()
room = []
heapq.heappush(room, lesson_list[0][1])

for i in range(1, N):
    if lesson_list[i][0] >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, lesson_list[i][1])

print(len(room))