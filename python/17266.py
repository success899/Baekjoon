import sys
input=sys.stdin.readline

N = int(input())
M = int(input())

x_list = list(map(int, input().split()))
len_x = len(x_list)

result = 0

if len_x == 1:
    result = max(x_list[0], N - x_list[0])

else:
    for i in range(len_x):
        if i == 0:
            height = x_list[i]
        elif i == len_x - 1:
            height = N - x_list[i]
        else:
            tmp = x_list[i] - x_list[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        result = max(height, result)

print(result)