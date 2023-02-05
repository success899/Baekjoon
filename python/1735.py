import sys, math
input=sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

bunjja = (A[0] * B[1]) + (B[0] * A[1])
bunmo = A[1] * B[1]

gcd = math.gcd(bunjja, bunmo)

bunjja = bunjja // gcd
bunmo = bunmo // gcd

print(bunjja, bunmo)