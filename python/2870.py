import sys
input=sys.stdin.readline

N = int(input())
result = []
nums = ['0','1','2','3','4','5','6','7','8','9']


for _ in range(N):
    num = str(input().rstrip())
    tmp = ''

    for i in num:
        if i in nums:
            tmp += i
        else:
            if tmp:
                result.append(int(tmp))
                tmp = ''
    
    if tmp:
        result.append(int(tmp))

result.sort()

for i in result:
    print(i)