import sys
input=sys.stdin.readline

num_list = []
num_index = []

for i in range(8):
    num_list.append(int(input()))

num_list_sort = sorted(num_list)
num_list_sort = num_list_sort[3:]

for i in range(8):
    for j in num_list_sort:
        if num_list[i] == j:
            num_index.append(i+1)

print(sum(num_list_sort))
for i in num_index:
    print(i, end=' ')