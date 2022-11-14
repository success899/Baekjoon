from collections import deque
import sys
input=sys.stdin.readline

N, K = map(int,input().split())
queue = deque([i for i in range(1,N+1)])
cnt = 0
result = '<'

while len(queue) > 0:
    cnt += 1
    if cnt % K == 0:
        result += str(queue.popleft()) + ', '
    else:
        queue.append(queue.popleft())
result = result[:-2]
result += '>'
print(result)