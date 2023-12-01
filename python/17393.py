import sys, bisect
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
result = []

for i, j in enumerate(A_list):
    result.append(bisect.bisect_right(B_list, j) - i - 1)
print(*result)