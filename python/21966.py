import sys
input=sys.stdin.readline

N = int(input())
S = str(input().rstrip())

if N <= 25:
    print(S)
elif '.' not in S[11:-12]:
    print(S[:11] + '...' + S[-11:])
else:
    print(S[:9] + '......' + S[-10:])