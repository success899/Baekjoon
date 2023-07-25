import sys, math
input=sys.stdin.readline

M = int(input())
color_list = list(map(int, input().split()))
K = int(input())
list_sum = sum(color_list)

total = math.comb(list_sum, K)
tmp = 0

for i in color_list:
    tmp += math.comb(i, K)

print(tmp/total)