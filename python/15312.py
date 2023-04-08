import sys
input=sys.stdin.readline

A = str(input().rstrip())
B = str(input().rstrip())

hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
#       A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
result = []
for i in range(len(A)):
    result.append(hint[ord(A[i]) - 65])
    result.append(hint[ord(B[i]) - 65])

tmp = []

while len(result) != 2:
	for i in range(len(result)-1):
		tmp.append((result[i] + result[i+1]) % 10)

	result = tmp
	tmp = []

print(result[0], end='')
print(result[1])