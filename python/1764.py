import sys
input=sys.stdin.readline

N, M = map(int,input().split())
N_list, M_list = set(), set()

for _ in range(N):
    N_list.add(input().strip())
for _ in range(M):
    M_list.add(input().strip())

result = sorted(list(N_list & M_list))

print(len(result))
for i in result:
    print(i)