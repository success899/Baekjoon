import sys
input=sys.stdin.readline

S = str(input().rstrip())
result = ''

for i in range(len(S)):
    if 65 <= ord(S[i]) <= 90:
        tmp = ord(S[i]) + 13
        if tmp > 90:
            tmp -= 26
        result += chr(tmp)
    elif 97 <= ord(S[i]) <= 122:
        tmp = ord(S[i]) + 13
        if tmp > 122:
            tmp -= 26
        result += chr(tmp)
    else:
        result += S[i]

print(result)