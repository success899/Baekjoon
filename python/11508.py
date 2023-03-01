import sys
input=sys.stdin.readline

N = int(input())
free = 0
price_list = []

for _ in range(N):
    price = int(input())
    price_list.append(price)

price_list.sort(reverse=True)

for i in range(2,N,3):
    free += price_list[i]

print(sum(price_list) - free)