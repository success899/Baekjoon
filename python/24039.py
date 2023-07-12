import sys
input=sys.stdin.readline

N = int(input())

check = [False] + [True]*103
tmp_list = []
result_list = []

for i in range(2, 104):
    if check[i]:
        tmp_list.append(i)
        for j in range(2*i, 104, i):
            check[j] = False

for i in range(1, len(tmp_list)):
    result_list.append(tmp_list[i] * tmp_list[i-1])

for i in result_list:
    if i > N:
        print(i)
        break