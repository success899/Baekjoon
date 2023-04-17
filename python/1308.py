import sys, datetime
input=sys.stdin.readline

start_day = list(map(int, input().split()))
end_day = list(map(int, input().split()))

start_day_date = datetime.date(start_day[0], start_day[1], start_day[2])
end_day_date = datetime.date(end_day[0], end_day[1], end_day[2])

gg_day_date_1000_start = datetime.date(start_day[0]+1000, start_day[1], start_day[2])
result = end_day_date - start_day_date


if end_day_date >= gg_day_date_1000_start:
    print('gg')
else:
    print(f'D-{result.days}')