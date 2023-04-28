import sys
input=sys.stdin.readline

N, game = map(str, input().rstrip().split())
N = int(N)
name = []

for _ in range(N):
    name.append(str(input().rstrip()))

name = set(name)

if game == 'Y':
    print(len(name))
elif game == 'F':
    print(len(name)//2)
elif game == 'O':
    print(len(name)//3)