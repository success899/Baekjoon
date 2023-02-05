import sys
input=sys.stdin.readline

A, B, C, D = map(str, input().split())

A_B = int(A + B)
C_D = int(C + D)

print(A_B + C_D)