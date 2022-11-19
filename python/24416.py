# 시간초과로 pypy3로 실행
import sys
input=sys.stdin.readline

N = int(input())
count_1 = 1
count_2 = 0

def fib(n):
    global count_1
    if n == 1 or n == 2:
        return 1
    else:
        count_1 += 1
        return fib(n-1) + fib(n - 2)

def fibonacci(n):
    global count_2
    f = [1] * (n + 1)
    for i in range(3, n + 1):
        count_2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(N)
fibonacci(N)
print(count_1, count_2)