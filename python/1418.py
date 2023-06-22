import sys
input=sys.stdin.readline

N = int(input())
K = int(input())

result = 0
s = [0] * (N+1)

for i in range(2, N+1):
    if s[i] == 0:
        for j in range(i, N+1,i):
            if j % i == 0:
                s[j] = max(s[j], i)

for i in s:
    if i <= K:
        result += 1
print(result-1)