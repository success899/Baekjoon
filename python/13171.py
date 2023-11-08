import sys
input=sys.stdin.readline

A = int(input())
X = int(input())
result = 1
xtobin = bin(X)[2:][::-1]
tmp = []

for i in range(65):
    tmp.append(A)
    A = A ** 2
    A %= 1000000007
for i in range(len(xtobin)):
    if int(xtobin[i]) == 1:
        result *= tmp[i]
        result %= 1000000007
        
print(result)