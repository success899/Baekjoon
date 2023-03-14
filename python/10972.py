import sys
input=sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
break_point = False

for i in range(N-1, 0, -1):
    if num_list[i-1] < num_list[i]:
        for j in range(N-1, 0, -1):
            if num_list[i-1] < num_list[j]:
                num_list[i-1], num_list[j] = num_list[j], num_list[i-1]
                num_list = num_list[:i] + sorted(num_list[i:])
                print(*num_list)
                break_point = True
                break
    if break_point == True:
        break
else:
    print(-1)