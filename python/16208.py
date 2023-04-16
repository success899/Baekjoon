import sys
input=sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
tmp = sum(n_list)
result  = 0

for i in n_list:
    result += i * (tmp - i)
    tmp -= i
    
print(result)