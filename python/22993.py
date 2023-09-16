import sys
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
power = A_list[0]
A_list_sort = sorted(A_list[1:])
result = True

for i in A_list_sort:
    if power > i:
        power += i
    else:
        result = False
        break

if result == True:
    print('Yes')
else:
    print('No')