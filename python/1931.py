n = int(input())

time_table = []

for _ in range(n):
    a, b = map(int, input().split())
    time_table.append((b, a))

time_table.sort()
a_time = 0
meeting_cnt = 0

for d, s in time_table:
    if s >= a_time:
        a_time = d
        meeting_cnt += 1

print(meeting_cnt)