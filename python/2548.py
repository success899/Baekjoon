import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

if N % 2 == 0:
    print(N_list[N//2 -1])

else:
    print(N_list[N // 2])