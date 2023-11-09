import sys
input=sys.stdin.readline

S = list(input())
tmp1, tmp2 = S.count('0') // 2, S.count('1') // 2

for _ in range(tmp1):
    S.pop(-S[::-1].index('0')-1)
for _ in range(tmp2):
    S.pop(S.index('1'))

print(''.join(S))