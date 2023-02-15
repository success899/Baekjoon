import sys
input=sys.stdin.readline

while True:
    S = str(input().rstrip())
    
    if S == '.':
        break

    stack = []
    result = 1

    for i in S:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = 0
                break
            elif stack[-1] == '[':
                stack.pop()

    if result and len(stack) == 0:
        print('yes')
    else:
        print('no')