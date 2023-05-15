import sys
input=sys.stdin.readline

N = int(input())
nums = []
result = 5
for i in range(N):
    nums.append(int(input()))
for i in range(N):
    count_1 = 4
    count_2 = 4
    for j in range(N):
       if nums[i]+5 > nums[j] and nums[i] < nums[j]:
           count_1 -= 1
       elif nums[i]-5 < nums[j] and nums[i] > nums[j]:
           count_2 -= 1     
    result = min(result, count_1, count_2)
print(result)