import sys
input=sys.stdin.readline

N, K = map(int, input().split())
table = list(map(str, input().rstrip()))
result = 0

for i in range(N):
    if table[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and table[j] == 'H':
                result += 1
                table[j] = 'E'
                break

print(result)