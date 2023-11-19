import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
result = True

for i in range(N):
    if i % 2:
        if N_list[i] % 2:
            result = False

print("YES" if result else "NO")