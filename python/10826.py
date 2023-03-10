import sys
input=sys.stdin.readline

N = int(input())

num = [0, 1]

for i in range(1,N):
    tmp = num[i] + num[i-1]
    num.append(tmp)

if N == 0:
    print(0)
else:
    print(num[-1])