import sys, math
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    N_list = list(map(int,input().split()))
    gcd = math.gcd(N_list[0],N_list[1])
    print(int(N_list[0]*N_list[1]/gcd))