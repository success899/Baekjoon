import sys
input=sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
J_list = []
index = 1
count = 0

for _ in range(J):
    J_list.append(int(input()))

for i in J_list:
    if index <= i and index + (M-1) >= i:
        pass
    elif index > i:
        count += abs(i - index)
        index = i
    else:
        count += i - (M-1) - index
        index = i - (M-1)
        
print(count)