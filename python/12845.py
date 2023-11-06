import sys
input=sys.stdin.readline

n = int(input())

L_list = list(map(int, input().split()))
L_list.sort(reverse=True)
result = 0

for i in range(len(L_list) - 1):
    i = 0
    result += L_list[i] + L_list[i+1]
    del L_list[i+1]
 
print(result)