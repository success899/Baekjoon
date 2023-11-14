import sys
input=sys.stdin.readline

N = int(input())
N_list = sorted(map(int, input().split()))
result = 0

for i in range(N-1):
    s, e = i+1, N-1
    t = -1
    while s <= e:
        m = (s+e)//2
        if N_list[i] >= 0.9 * N_list[m]:
            t = m
            s = m + 1
        else:
            e = m - 1
    result += t-i if t > -1 else 0
print(result)