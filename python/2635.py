import sys
input=sys.stdin.readline

N = int(input())
len_size = 0
result = []

for i in range(N+1):
    tmp_list = [N, i]
    j = 0
    while True:
        last_num = tmp_list[j] - tmp_list[j+1]
        j += 1
        if last_num < 0:
            break
        tmp_list.append(last_num)
        if len_size < len(tmp_list):
            len_size = len(tmp_list)
            result = tmp_list[:]

print(len_size)
result_list = [str(result[i]) for i in range(len(result))]
print(' '.join(result_list))