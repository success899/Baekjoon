import sys
input=sys.stdin.readline

N = int(input())
A = set(list(map(int, input().split())))

is_prime = [False, False] + [True] * (1000000 - 1)
for i in range(2, len(is_prime)):
    if not is_prime[i]:
        continue
    for j in range(2 * i, len(is_prime), i):
        is_prime[j] = False

result = 1
for num in A:
    if is_prime[num]:
        result *= num

if result == 1:
    result *= -1
print(result)