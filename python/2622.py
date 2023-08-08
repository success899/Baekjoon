import sys, math
input=sys.stdin.readline

N = int(input())
result = 0

for x in range(math.ceil(N/3), math.ceil(N/2)):
    for y in range(math.ceil((N - x)/2), x + 1):
        result += 1

print(result)