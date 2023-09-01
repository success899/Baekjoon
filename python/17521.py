import sys
input=sys.stdin.readline

n, W = map(int, input().split())
price_list = []
amount = 0

for _ in range(n):
    price_list.append(int(input()))

for i in range(n-1):
    if price_list[i] < price_list[i+1]:
        if W // price_list[i] > 0:
            amount = W // price_list[i]
            W = W - (amount * price_list[i])
    elif price_list[i-1] < price_list[i] and amount > 0:
        W = W + amount * price_list[i]
        amount = 0

if amount > 0:
    W = W + amount * price_list[n-1]

print(W)