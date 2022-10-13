def pibo(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    return pibo(n-1) + pibo (n-2)

num = int(input())
if 0 <= num <=20:
    print(pibo(num))