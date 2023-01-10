import sys
input=sys.stdin.readline

N, K = map(int, input().split())
people_list = [i for i in range(1,N+1)]
result = []
idx = 0

for _ in range(N):
    idx += K-1
    if idx >= len(people_list):
        idx = idx%len(people_list)
    result.append(str(people_list.pop(idx)))

print(f'<{", ".join(result)}>')