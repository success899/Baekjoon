import sys
input=sys.stdin.readline

N = int(input())

num_list = list(map(int,input().split()))
num_list = list(set(num_list))
num_list.sort()

for i in num_list:
    print(i, end=' ')