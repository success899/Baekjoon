import sys, collections
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
A_list.reverse()
dq = collections.deque()

for i in range(N):
    if A_list[i] == 1:
        dq.appendleft(i + 1)
    elif A_list[i] == 2:
        dq.insert(1, i + 1)
    elif A_list[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")