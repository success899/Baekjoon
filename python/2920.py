import sys
input=sys.stdin.readline

num = list(map(int, input().split()))
tmp = list(num)

tmp.sort()
if num == tmp:
    print('ascending')
else:
    tmp.sort(reverse=True)
    if num == tmp:
        print('descending')
    else:
        print('mixed')