import sys
input=sys.stdin.readline

import sys
N, A, D = map(int, input().split())
N_list = list(map(int, input().split()))

result, X = 0, 0

for i in range(N):
    if N_list[i] == A + (X*D):
        result += 1
        X += 1
print(result)