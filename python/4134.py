import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tmp = False

    if n == 0 or n == 1:
            print(2)

    else:
        while True:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    n += 1
                    break
            else:
                print(n)
                tmp = True
                break