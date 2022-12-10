import sys, re
input=sys.stdin.readline

S = input().split('-')
num_list = []

for i in S:
    tmp = 0
    split_tmp = i.split('+')
    for j in split_tmp:
        tmp += int(j)
    num_list.append(tmp)

result = num_list[0]

for i in range(1,len(num_list)):
    result -= num_list[i]

print(result)