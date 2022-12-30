import sys
input=sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = list(map(str,input().split()))
    if len(command) == 2:
        cal, x = command[0], int(command[1])
    else:
        cal = command[0]

    if cal == 'add':
        S.add(x)

    elif cal == 'remove':
        S.discard(x)

    elif cal == 'check':
        if x in S:
            print('1')
        else:
            print('0')

    elif cal == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)

    elif cal == 'all':
        S = set([i for i in range(1, 21)])

    elif cal == 'empty':
        S = set()