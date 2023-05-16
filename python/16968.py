import sys
input=sys.stdin.readline

S = str(input().rstrip())

if S[0] == 'c':
    result = 26
elif S[0] == 'd':
    result = 10

for i in range(1, len(S)):
    if S[i] == 'c':
        if S[i - 1] == 'c':
            result *= 25
        else:
            result *= 26
    elif S[i] == 'd':
        if S[i - 1] == 'd':
            result *= 9
        else:
            result *= 10

print(result)