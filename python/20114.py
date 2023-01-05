import sys
input=sys.stdin.readline

N, H, W = map(int, input().split())

words = []
result = ""

for _ in range(H):
    words.append(input().rstrip())

for i in range(N):
    tmp = '?'
    for j in range(W*i, W*(i+1)):
        for k in range(H):
            if words[k][j]!='?':
                tmp = words[k][j]

    result += tmp

print(result)