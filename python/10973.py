import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if N_list[i] < N_list[i-1]:
        x, y = i-1, i
        for j in range(N-1, 0, -1):
            if N_list[j] < N_list[x]:
                N_list[j], N_list[x] = N_list[x], N_list[j]
                N_list = N_list[:i] + sorted(N_list[i:], reverse=True)
                print(*N_list)
                exit(0)
print(-1)