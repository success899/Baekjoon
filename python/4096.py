import sys
input=sys.stdin.readline

while True:
    n = str(input().rstrip())
    count = 0
    if n == '0':
        break

    elif n == n[::-1] :
        print(count)
        
    else:
        tmp = len(n)
        while n != n[::-1]:
            count += 1
            t = int(n) + 1
            n = str(t).zfill(tmp)
        print(count)