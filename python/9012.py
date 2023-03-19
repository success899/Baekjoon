import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    VPS = list(map(str, input().rstrip()))

    for i in VPS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')