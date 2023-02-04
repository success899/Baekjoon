import math
import sys
input=sys.stdin.readline

t = int(input())

for i in range(t):
    test_list = list(map(int, input().split()))
    result = 0

    for j in range(1, test_list[0]+1):
        for k in range(j+1, test_list[0]+1):
            result+=math.gcd(test_list[j], test_list[k])

    print(result)