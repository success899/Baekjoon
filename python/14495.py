import sys
input=sys.stdin.readline

n = int(input())
num_list = [1, 1, 1]

for i in range(3,n):
    num_list.append(num_list[i-1] + num_list[i-3])

print(num_list[-1])