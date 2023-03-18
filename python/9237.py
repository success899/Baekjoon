import sys
input=sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

for i in range(N):
    t[i] = t[i] + i + 1

print(max(t)+1)