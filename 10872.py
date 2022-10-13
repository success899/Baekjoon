def factorial(n):
    if n == 1:
        return 1
    return n * factorial (n-1)

num = int(input())
if num == 0:
    print(1)
elif 0 <= num <=12:
    print(factorial(num))