import sys, itertools
input=sys.stdin.readline

height_list = []

for _ in range(9):
    height_list.append(int(input()))

for i in itertools.combinations(height_list, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break