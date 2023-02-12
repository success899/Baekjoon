import sys
input=sys.stdin.readline

N = int(input())
files = {}

for _ in range(N):
    _, tmp = map(str, input().rstrip().split('.'))

    if tmp in files:
        files[tmp] += 1
    else:
        files[tmp] = 1

for i in sorted(files.items()):
    print(i[0], i[1])