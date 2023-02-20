import sys
input=sys.stdin.readline

S = list(str(input().rstrip()))
start, index = 0, 0

while index < len(S):
    if S[index] == '<':
        index += 1
        while S[index] != '>':
            index += 1
        index += 1

    elif S[index].isalnum():
        start = index
        while index < len(S) and S[index].isalnum():
            index += 1
        tmp = S[start:index]
        tmp.reverse()
        S[start:index] = tmp
    
    else:
        index += 1

print(''.join(S))