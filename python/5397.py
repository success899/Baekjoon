import sys
input=sys.stdin.readline

for _ in range(int(input())):
    L = str(input().rstrip())
    left, right = [], []

    for i in L:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))

    for i in left:
        print(i, end='')
    print()