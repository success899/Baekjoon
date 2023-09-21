import sys, math
input=sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
X = int(input())

result = [0, 0]
for i in A_list:
    if math.gcd(i, X) == 1:
        result[0] += i
        result[1] += 1

print(result[0]/result[1])