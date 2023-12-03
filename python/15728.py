import sys
input=sys.stdin.readline

N, K = map(int, input().split())
share = list(map(int, input().split()))
team = set((map(int, input().split())))

for _ in range(K):
    s = -int(1e9)
    x = 0
    for i in team:
        for j in share:
            if s <= i*j:
                s = i*j
                x = i
    team.remove(x)
result = -int(1e9)

for i in team:
    for j in share:
        result = max(result, i*j)
        
print(result)