def merge_sort(num):
    if len(num) < 2:
        return num

    mid = int(len(num) // 2)
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])

    num_list = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            num_list.append(left[l])
            l += 1
        else:
            num_list.append(right[r])
            r += 1
    num_list += left[l:]
    num_list += right[r:]
    return num_list

n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))
num_list = merge_sort(num_list)
for i in range(n):
    print(num_list[i])