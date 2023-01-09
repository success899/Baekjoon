import sys
input=sys.stdin.readline

N1 = list(input().rstrip())
N2 = []
M = int(input())

for _ in range(M):
    command = list(input().split())

    if command[0] == 'L':
        if N1:
            N2.append(N1.pop())

    elif command[0] == 'D':
        if N2:
            N1.append(N2.pop())

    elif command[0] == 'B':
        if N1:
            N1.pop()

    else:
        N1.append(command[1])
    

N1.extend(reversed(N2))
print(''.join(N1))