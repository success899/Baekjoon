n = int(input())

for i in range(1, n+1) :  
    num_list = list(map(int, str(i)))
    result = i + sum(num_list)
    if result == n:
        print(i)
        break

    elif i==n:
        print(0)