import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num = 2
    result_dic = {}
    
    for i in range(n+1):
        result_dic[i] = 0

    while True:
        if n == 1:
            break
        if n % num != 0:
            num += 1
        else:
            n /= num
            result_dic[num] += 1

    for i in result_dic.items():
        if i[1] != 0:
            print(i[0], i[1])