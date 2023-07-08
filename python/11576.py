import sys, math
input=sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
m_list = list(map(int, input().split()))
tmp = 0
result = []

for i in range(m):
    tmp += int(m_list[i] * math.pow(A, m - i - 1))

while tmp:
    temp = tmp % B
    result.append(str(temp))
    tmp = tmp // B

result = result[::-1]
for i in result:
    print(i, end=' ')