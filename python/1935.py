import sys
input=sys.stdin.readline

N = int(input())
postfix_notation = list(input().rstrip())
num = [int(input()) for i in range(N)]
tmp = []

for i in postfix_notation:
    if i.isalpha():
        tmp.append(num[ord(i)-65])
    else:
        a = tmp.pop()
        result = tmp.pop()

        if i == '+':
            result += a

        elif i == '-':
            result -= a

        elif i == '*':
            result *= a

        elif i == '/':
            result /= a

        tmp.append(result)

print('%.2f' %tmp[-1])