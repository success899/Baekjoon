import sys
input=sys.stdin.readline

tmp = list(map(int, input().split()))
n_list = []

if len(tmp) > 1:
    n = tmp[0]
    n_list.extend(tmp[1:])
else:
    n = tmp[0]

while len(n_list) != n:
    n_list.extend(map(int, input().split()))

for i in range(n):
    n_list[i] = int(str(n_list[i])[::-1])
    
n_list.sort()
print(*n_list, sep='\n')