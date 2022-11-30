import sys
input=sys.stdin.readline

S = input().strip()
S_tmp = set()

for i in range(len(S)):
    for j in range(i,len(S)):
        S_tmp.add(S[i:j+1])

print(len(S_tmp))