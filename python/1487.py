import sys
input=sys.stdin.readline

N = int(input())
amount_list = []
fee_list = []

for i in range(N):
	amount, fee = map(int,input().split())
	amount_list.append(amount)
	fee_list.append(fee)

amount_set = sorted(set(amount_list))
max_price = 0 
result = 0

for i in amount_set:
	price = 0
	for j in range(N):
		if i <= amount_list[j] and i > fee_list[j]:
			price += i-fee_list[j]
	
	if max_price < price:
		max_price = price
		result = i
	
print(result)