import sys
input=sys.stdin.readline

X, Y = map(str, input().split())

X, Y = X[::-1], Y[::-1]
A_sum_B = int(str(int(X) + int(Y))[::-1])

print(A_sum_B)