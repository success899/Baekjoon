N, X = input().split()
N = int(N)
X = int(X)
A = input()
A = A.split()

for i in range(N):
    if int(A[i]) < X :
        print(A[i], end=" ")