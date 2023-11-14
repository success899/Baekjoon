import sys
input=sys.stdin.readline


timetable = [[600, 600], [1320, 1320]]
 
for _ in range(int(input())):
    start, end = input().split()
    s_time = (int(start[:2]) * 60) + int(start[2:]) - 10
    e_time = (int(end[:2]) * 60) + int(end[2:]) + 10
    timetable.append([s_time, e_time])
 
timetable.sort()
 
result = 0
tmp = 600

for s, e in timetable:
    result = max(result, s - tmp)
    tmp = max(tmp, e)
 
print(result)