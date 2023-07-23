import sys
input=sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0 :
        break

    n_sub_k = n - k
    a, b = 1, 1

    for i in range(n, max(k, n_sub_k), -1):
        a *= i
    for i in range(1, min(n_sub_k, k)+1):
        b *= i

    print(a // b)