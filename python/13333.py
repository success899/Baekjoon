import sys
input=sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))

for i in range(n,-1,-1):
  if i <= n_list[-i]:
    print(i)
    break