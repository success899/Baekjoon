import sys
input=sys.stdin.readline

n, count1, count2 = int(input()), 0, 0
a_list = list(map(int, input().split()))
tmp = sum(a_list) // n

for i in a_list:
    if i > tmp + 1:
        count1 += (i - tmp - 1)
    elif i < tmp:
        count2 += (tmp - i)
    
print(max(count1, count2))