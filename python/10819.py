import sys, itertools
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

P = list(itertools.permutations(A, N))

def calculator(i):
    total = 0

    for j in range(len(i) - 1):
        total += abs(i[j] - i[j+1])

    return total

result = -1e9

for i in P:
    result = max(result, calculator(i))

print(result)