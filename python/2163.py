import sys
input=sys.stdin.readline

N, M = map(int, input().split())

result = (N-1+((M-1)*N))
print(result)