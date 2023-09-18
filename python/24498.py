import sys
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))

if N<=2:
    print(max(A_list))
else:
    result = [A_list[0], A_list[N-1]]

    for i in range(1, len(A_list) -1):
        result.append(A_list[i] + min(A_list[i+1], A_list[i-1]))

    print(max(result))