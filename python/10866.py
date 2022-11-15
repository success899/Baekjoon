import sys
input=sys.stdin.readline

n = int(input())

stack = []
point = -1

for i in range(n):
    c = list(input().split())
    
    if c[0] == "push_front":
        c[1] = int(c[1])
        stack.insert(0, c[1])
        point += 1
    elif c[0] == "push_back":
        c[1] = int(c[1])
        stack += [c[1]]
        point += 1
    elif c[0] == "pop_front":
        if point >= 0:
            print(stack[0])
            del stack[0]
            point -= 1
        else :
            print(-1)
    elif c[0] == "pop_back":
        if point >= 0:
            print(stack[-1])
            del stack[-1]
            point -= 1
        else :
            print(-1)

    elif c[0] == "size":
        print((point+1))
    elif c[0] == "empty":
        if point == -1 :
            print(1)
        else:
            print(0)
    elif c[0] == "front":
        if point >= 0:
            print(stack[0])
        else :
            print(-1)
    elif c[0] == "back":
        if point >= 0:
            print(stack[-1])
        else :
            print(-1)