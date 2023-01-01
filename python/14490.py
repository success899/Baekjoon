import sys, math
input=sys.stdin.readline

n, m = map(int, input().split(':'))
tmp = math.gcd(n,m)

print(f'{n//tmp}:{m//tmp}')