import sys
input=sys.stdin.readline

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
result = 0
for i in range(x-1):
    result += month[i]

day = (result + y) % 7

print(week[day])