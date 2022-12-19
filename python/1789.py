import sys
input=sys.stdin.readline

S = int(input())
N = 0
tmp = 0

while True:
    if S < tmp:
        print(N-1)
        break
    N += 1
    tmp += N