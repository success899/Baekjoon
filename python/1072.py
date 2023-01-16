import sys
input=sys.stdin.readline

X, Y = map(int, input().split())
tmp = (Y * 100) // X

if tmp >= 99:
    print(-1)
else:
    start, end = 1, X

    while start <= end:
        mid = (start + end) // 2
        if (Y + mid) * 100 // (X + mid) <= tmp:
            start = mid + 1
        else:
            end = mid - 1
    print(end + 1)