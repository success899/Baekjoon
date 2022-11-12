n, k = map(int, input().split())

cnt = 0
a = []

for _ in range(n):
    a.append(int(input()))

for i in a[::-1]:
    cnt = cnt + k//i
    k = k % i

print(cnt)