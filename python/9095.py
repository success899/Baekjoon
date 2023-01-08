import sys
input=sys.stdin.readline

tmp_list = [0] * 11
tmp_list[1] = 1
tmp_list[2] = 2
tmp_list[3] = 4

for i in range(4, 11):
    tmp_list[i] = sum(tmp_list[i-3:i])

T = int(input())
for _ in range(T):
    n = int(input())
    print(tmp_list[n])