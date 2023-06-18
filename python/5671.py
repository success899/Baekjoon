import sys
input=sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
    except:
        break
    result = 0
    for i in range(N,M+1):
        count = set()
        sum_i = str(i)
        for j in sum_i:
            count.add(j)
        if len(sum_i) == len(count):
            result += 1
    print(result)