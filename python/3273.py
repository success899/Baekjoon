import sys
input=sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

count, start, end = 0, 0, len(a)-1

a.sort()

while start < end:
    if a[start] + a[end] > x:
        end -= 1
    elif a[start] + a[end] < x:
        start += 1
    elif a[start] + a[end] == x:
        count += 1
        start += 1
        end -= 1

print(count)