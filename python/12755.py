import sys
input=sys.stdin.readline

N = int(input())

count = 0
num = 1

while True:
    length = len(str(num))
    count += length

    if count >= N:
        nums = str(num)
        index = N - (count - length) - 1
        print(nums[index])
        break

    num += 1