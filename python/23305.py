import sys
input=sys.stdin.readline

N = int(input())
nums = [0] * 1000001
result = 0

for i in list(map(int, input().split())):
    nums[i] += 1

for i in list(map(int, input().split())):
    if nums[i] >= 1:
        nums[i] -= 1
    else:
        result += 1

print(result)