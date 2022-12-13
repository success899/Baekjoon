import sys
input=sys.stdin.readline

def merge_sort(num):
    if len(num) == 1:
        return num

    mid = (len(num)+1) // 2

    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])

    num_list = []
    l,r = 0,0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            num_list.append(left[l])
            num_result.append(left[l])
            l += 1
        else:
            num_list.append(right[r])
            num_result.append(right[r])
            r += 1

    while l < len(left):
        num_list.append(left[l])
        num_result.append(left[l])
        l += 1

    while r < len(right):
        num_list.append(right[r])
        num_result.append(right[r])
        r += 1

    return num_list

A, K = map(int,input().split())
A_arr = list(map(int,input().split()))
num_result = []
merge_sort(A_arr)

if len(num_result) >= K:
    print(num_result[K-1])
else:
    print(-1)