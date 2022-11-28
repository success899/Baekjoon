import sys
input=sys.stdin.readline

A, B = map(int,input().split())

A_list, B_list = set(), set()


tmp = list(map(int,input().split()))
for i in tmp:
    A_list.add(i)

tmp = list(map(int,input().split()))
for i in tmp:
    B_list.add(i)

print(len(A_list-B_list)+len(B_list-A_list))