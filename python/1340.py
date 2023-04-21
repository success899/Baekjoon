import sys
input=sys.stdin.readline

Month, D, Y, HM = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, HM.split(':'))
month_list = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    month_day[1] += 1
total_time = sum(month_day) * 24 * 60

last_month = month_list.index(Month)
now_time = (sum(month_day[:last_month]) + D-1) * 24 * 60 + (H * 60) + M

print(now_time/total_time * 100)