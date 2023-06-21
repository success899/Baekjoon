import sys
input=sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
num = []
num.append(n_list[0])
for i in range(1, n):
    num.append(num[i-1] + n_list[i])

result = 0
for i in range(n):
    result = result + n_list[i] * (num[n-1] - num[i])

print(result)