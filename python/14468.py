import sys
input=sys.stdin.readline

S = input().strip()
result = 0

for i in range(52):
    for j in range(i+1,52):
        if S[i] == S[j]:
            tmp = S[i:j+1]
            for i in tmp:
                if tmp.count(i) == 1:
                    result += 1
            break

print(result // 2)