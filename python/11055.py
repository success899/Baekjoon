import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

array = [1] * N
array[0] = A[0]

for i in range(1, N):
  for j in range(i):
    if A[j] < A[i]:
      array[i] = max(array[i], array[j] + A[i])
    else:
      array[i] = max(array[i], A[i])

print(max(array))