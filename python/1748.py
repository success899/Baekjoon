import sys
input=sys.stdin.readline

N = int(input())
len_N = len(str(N))
result = 0

for i in range(len_N-1):
    result += 9 * 10 ** i * (i+1)

print(result + (N - 10 ** (len_N-1) + 1) * len_N)