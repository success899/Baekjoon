import sys
input=sys.stdin.readline

A_team = list(map(int, input().split()))
B_team = list(map(int, input().split()))
result = False
tmp = 0

for i in range(9):
    tmp += A_team[i]
    if tmp > 0:
        result = True
    tmp -= B_team[i]

if tmp < 0 and result == True:
    print('Yes')
else:
    print('No')