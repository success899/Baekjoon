import sys
input=sys.stdin.readline

N = int(input())
M, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

pen = M * K
count = 0

for p in A:
    if pen > 0:
        count += 1
        pen -= p
    else:
        break

if pen > 0:
    print('STRESS')
else:
    print(count)