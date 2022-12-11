import sys
input=sys.stdin.readline

N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

result = 0
price_tmp = price[0]

for i in range(N-1):
    if price[i] < price_tmp:
        price_tmp = price[i]
    result = result + (price_tmp * distance[i])

print(result)