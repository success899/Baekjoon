n = int(input())
num_val = 2
while True:
    if n == 1:
        break
        
    if n % num_val == 0:
        n = n//num_val
        print(num_val)
    elif n % num_val != 0:
        num_val += 1
