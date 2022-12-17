import sys
input=sys.stdin.readline

N = 3
T = int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    num_list.sort()

    print(num_list[-N])