import sys
input=sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    c = list(map(str, input().split()))
    
    if c[0] == "push":
        c[1] = int(c[1])
        stack.append(c[1])
        
    elif c[0] == "pop":
        if len(stack) > 0:
            print(stack[0])
            del stack[0]
        else :
            print(-1)
    elif c[0] == "size":
        print(len(stack))
    elif c[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif c[0] == "front":
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)
    elif c[0] == "back":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)