import sys
input=sys.stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))

    if nums[0]*2 <= nums[1] and nums[1] % nums[0] == 0:
        print(1)
    else:
        print(0)