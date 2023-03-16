import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))


tmp, prefix_sum = 0, [0]

for i in range(N):
    tmp += N_list[i]
    prefix_sum.append(tmp)

for _ in range(int(input())):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i-1])