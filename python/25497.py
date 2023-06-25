import sys
input=sys.stdin.readline

N = int(input())
N_list = str(input().rstrip())
count = 0
L, S = 0, 0

for i in N_list:
    if i == 'L':
        L += 1
    elif i == 'R':
        if L > 0:
            count += 1
            L -= 1
        else:
            break	
    elif i == 'S':
        S += 1
    elif i == 'K':
        if S > 0:
            count += 1
            S -= 1
        else:
            break
    else:
        count += 1

print(count)