num_list = []
num_max = 0
for i in range(0,9):
    n = int(input())
    num_list.append(n)

    if len(num_list) > 1:
        if num_list[i] >= num_max:
            num_max = num_list[i]
    else:
        num_max = num_list[i]

print(num_max)

for i in range(0,9):
    if num_max == num_list[i]:
        print(i+1)