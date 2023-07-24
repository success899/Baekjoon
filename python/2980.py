import sys
input=sys.stdin.readline

N, L = map(int, input().split())
tmp = 0
result = 0

for _ in range(N):
    D, R, G = map(int, input().split())

    result += (D - tmp)
    tmp = D
    if result % (R+G) <= R:
        result += (R - (result%(R+G)))

result += (L-tmp)
print(result)