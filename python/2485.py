import sys, math
input=sys.stdin.readline


N = int(input())
first = int(input())
tree = []

for i in range(N-1):
    num = int(input())
    tree.append(num - first)
    first = num

tmp = tree[0]
for j in range(1, len(tree)):
    tmp = math.gcd(tmp, tree[j])

result = 0
for each in tree:
    result += each // tmp - 1
print(result)