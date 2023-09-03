import sys
input=sys.stdin.readline
from collections import deque

N = int(input())
li = []

for i in range(N):
    li.append(input().rstrip())

for i in range(N):
    deq = deque(li[i])
    while True:
        deq.append(deq.popleft())
        tmp = "".join(deq)
        if tmp == li[i]:
            break

        if tmp in li:
            idx = li.index(tmp)
            li.pop(idx)
            li.insert(idx, li[i])

li = set(li)
print(len(li))