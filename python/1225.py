import sys
input=sys.stdin.readline

A, B = map(str, input().split())
A, B = list(map(int, A)), list(map(int, B))

print(sum(A) * sum(B))