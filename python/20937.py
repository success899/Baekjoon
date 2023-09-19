import sys
input=sys.stdin.readline

num_list = [0] * 500001
N = int(input())
C_list = map(int, input().split())

for i in C_list:
    num_list[i] += 1
print(max(num_list))