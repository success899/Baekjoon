def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M = int(input())
N = int(input())
num_list = []

for i in range(M, N+1):
    if isPrime(i):
        num_list.append(i)
if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))