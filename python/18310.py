import sys
input=sys.stdin.readline

N = int(input())
N_list = []
N_list = list(map(int, input().split()))
N_list.sort()

print(N_list[(N-1)//2])