import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.append(int(input()))

    tmp_sum = sum(n_list)
    tmp_max = max(n_list)
    tmp_idx = n_list.index(tmp_max) + 1
    tmp_list = sorted(n_list, reverse=True)

    if tmp_list[0] == tmp_list[1]:
        print('no winner')
    else:
        if tmp_max > tmp_sum/2:
            print(f'majority winner {tmp_idx}')
        else:
            print(f'minority winner {tmp_idx}')