import sys
input=sys.stdin.readline

N = int(input())

time_list = list(map(int,input().split()))
time_list.sort()
result = 0
tmp = 0
for i in time_list:
    tmp += i
    result += tmp

print(result)