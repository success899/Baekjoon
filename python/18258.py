import sys
input=sys.stdin.readline

N = int(input())

queue = []
cnt = 0

for i in range(N):
    c = list(input().split())
    
    if c[0] == "push":
        c[1] = int(c[1])
        queue.append(c[1])
    elif c[0] == "pop":
        if len(queue)-cnt <= 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1
    elif c[0] == "size":
        print((len(queue)-cnt))
    elif c[0] == "front":
        if len(queue)-cnt <= 0:
            print(-1)
        else:
            print(queue[cnt])
    elif c[0] == "back":
        if len(queue)-cnt <= 0:
            print(-1)
        else:
            print(queue[-1])
    elif c[0] == "empty":
        if len(queue)-cnt <= 0:
            print(1)
        else:
            print(0)