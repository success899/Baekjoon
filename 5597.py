n_list = [0] * 30

for i in range(0,28):
    n = int(input())
    n_list[n-1] += 1

for i in range(0,30):
    if n_list[i] == 0:
        print(i+1)