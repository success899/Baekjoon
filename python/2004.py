import sys
input=sys.stdin.readline

N, K = map(int,input().split())

def func(n, num):
    count = 0
    while n:
        n = n // num
        count += n
    return count

count_five = func(N, 5) - func(K, 5) - func(N - K, 5)
count_two = func(N, 2) - func(K, 2) - func(N - K, 2)

print(min(count_five, count_two))