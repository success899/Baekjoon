num_list = []
num_rest = []

for i in range(0,10):
    num_list.append(int(input()))

for i in range(0,len(num_list)):
    num_rest.append(num_list[i] % 42)

num_set = set(num_rest)

print(len(num_set))