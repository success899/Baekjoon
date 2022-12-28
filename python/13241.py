import sys, math
input=sys.stdin.readline

A, B = map(int,input().split())

print(A*B//math.gcd(A,B))