import sys
input=sys.stdin.readline

N, K = map(int,input().split())

def func(n):
    tmp = 1
    if n == 0:
        return tmp
    for i in range(1,n+1):
        tmp *= i
    return tmp

print((func(N) // (func(K) * func(N - K)))%10007)