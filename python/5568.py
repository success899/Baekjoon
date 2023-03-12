from itertools import permutations
import sys
input=sys.stdin.readline

n, k = int(input()), int(input())

n_list = []
result = set()

for _ in range(n):
    n_list.append(str(input().rstrip()))

for i in permutations(n_list, k):
    result.add(''.join(i))

print(len(result))