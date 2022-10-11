n = int(input())
num_list = []

for i in range(0,n):
    num_list.append(int(input()))
num_list.sort()
for i in range(0,n):
    print(num_list[i])