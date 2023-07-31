import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N = input().rstrip()
    tmp = 5 * (10 ** (len(N)-1)) - 1
    num1 = ''
    num2 = ''
    
    if int(N) >= tmp:
        num1 = tmp + 1
        num2 = tmp
        
    else:
        num1 = int(N)
        
        for i in N:
            num2 += str(9 - int(i))
        num2 = int(num2)
        
    print(num1 * num2)