import sys
input=sys.stdin.readline

N, C = map(int, input().split())
message = list(map(int, input().split()))
tmp = {}

for i in range(N):
    if message[i] in tmp :
        tmp[message[i]][0] += 1
    else :
        tmp[message[i]] = [1, i]

result = sorted(tmp.items(), key= lambda x: (-x[1][0], x[1][1]))
goal = []

for i in result:
    for j in range(i[1][0]) :
        goal.append(str(i[0]))

print(" ".join(goal))