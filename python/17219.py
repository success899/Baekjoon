import sys
input=sys.stdin.readline

N, M = map(int, input().split())
N_list = {}

for _ in range(N):
    site, password = map(str, input().split())
    N_list[site] = password

for _ in range(M):
    find_site = input().rstrip()
    print(N_list[find_site])