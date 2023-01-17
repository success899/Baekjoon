import sys
input=sys.stdin.readline

N = int(input())
price_list = list(map(int,input().split()))
M = int(input())

start, end = 0, max(price_list)

if sum(price_list) <= M:
    print(end)
else:
    while start <= end:
        mid = (start + end) // 2
        result = 0

        for i in price_list:
            result += min(mid, i)
        if result > M:
            end = mid - 1
            last_point = True
        else:
            start = mid + 1
            last_point = False
            
    if last_point:
        print(mid-1)
    else:
        print(mid)