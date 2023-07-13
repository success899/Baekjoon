import sys
input=sys.stdin.readline

k = int(input())
a, b, c, d = list(map(int, input().split()))

num1 = a*k + b
num2 = c*k + d

if num1 == num2:
    print("Yes", num1)
else:
    print("No")