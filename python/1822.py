import sys
input=sys.stdin.readline

N = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = A-B
print(len(result))

if len(result) !=0:
    result = sorted(result)
    print(*(result))