import sys
input=sys.stdin.readline

N = int(input())
a_arr = list(map(int, input().split()))
a_arr.sort()

print(*a_arr)