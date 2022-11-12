import sys, math
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))

for i in range(1,N):
    gcd = math.gcd(N_list[0],N_list[i])
    print((str(N_list[0]//gcd)+'/'+str(N_list[i]//gcd)).strip())