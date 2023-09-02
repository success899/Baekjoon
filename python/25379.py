import sys
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
result1, result2 = 0, 0
tmp = 0

for i in A_list:
    if i%2 == 1:
        tmp+=1
    else:
        result1 += tmp
A_list.reverse()
tmp = 0

for i in A_list:
    if i%2 == 1:
        tmp += 1
    else:
        result2 += tmp
print(min(result1, result2))