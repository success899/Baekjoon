import sys

input=sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    K = int(input())
    if K != 0:
        stack.append(K)
    elif K == 0:
        stack = stack[:-1]

print(sum(stack))