import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    input_str = list(map(str, input().split()))
    result = []
    for i in input_str:
        result.append(i[::-1])
    print(' '.join(result))