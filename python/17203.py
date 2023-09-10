import sys
input=sys.stdin.readline

N, Q = map(int, input().split())
a_list = list(map(int, input().split()))

for _ in range(Q):
    i, j = map(int, input().split())
    result = 0

    if j-1 < i:
        print(result)
    else:
        for i in range(i-1, j-1):
            result += abs(a_list[i] - a_list[i+1])
        print(result)