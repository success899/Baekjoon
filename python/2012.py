import sys
input=sys.stdin.readline

N = int(input())
rank = []
result = 0

for _ in range(N):
    rank.append(int(input()))

rank.sort()

for i in range(N):
    tmp = i+1
    result += abs(tmp - rank[i])

print(result)