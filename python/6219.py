import sys
input=sys.stdin.readline

A, B, D = map(int, input().split())
num_list = [1] * (B + 1)

for i in range(2, int(B**0.5)+1):
    if num_list[i]:
        for j in range(i+i, B+1, i):
            num_list[j] = 0

prime = [i for i in range(A, B+1) if num_list[i]]

result = 0
for n in prime:
    if str(D) in str(n):
        result += 1
        
print(result)