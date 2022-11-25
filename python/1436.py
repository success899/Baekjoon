import sys
input=sys.stdin.readline

N = int(input())

count, tmp = 0, 0

while(True):
    tmp += 1

    if '666' in str(tmp):
        count += 1

    if count == N:
        print(tmp)
        break