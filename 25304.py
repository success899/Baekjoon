x = int(input())
n = int(input())
 
for i in range(n):
    price, amount = input().split()
    price, amount = int(price), int(amount)
    
    x -= (price*amount)
    
if x == 0:
    print("Yes")
else:
    print("No")