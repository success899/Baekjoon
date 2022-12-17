import sys
input=sys.stdin.readline

N = str(input().rstrip())
num_list = [0] * 10

for i in range(len(N)):
    num_list[int(N[i])] += 1
tmp = ((num_list[6] + num_list[9])//2)+((num_list[6] + num_list[9])%2)
del num_list[9]
del num_list[6]

print(max(max(num_list), tmp))