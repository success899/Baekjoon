import sys, itertools
input=sys.stdin.readline

N, K = map(int, input().split())
K_list = list(map(str, input().split()))
result_len = len(str(N))

while True:
    tmp = list(itertools.product(K_list, repeat = result_len))
    result = []

    for i in tmp:
        if int("".join(i)) <= N:
            result.append(int("".join(i)))
    
    if len(result) >= 1:
        print(max(result))
        break
    
    else:
        result_len -= 1