n = int(input())
num_list = list(map(int,input().split()))
num_cnt = n

for i in num_list:
    if i == 1:
        num_cnt -= 1

    for y in range(2,i):
        if i % y == 0:
            num_cnt -= 1
            break
print(num_cnt)