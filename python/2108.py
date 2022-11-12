import sys

n = int(sys.stdin.readline())
num_list = []
num_set = []
num_cnt_dic = {}
if 1 <= n <= 500000 and (n == 1 or n % 2 == 1):         # 1~500000사이 값 + n은 홀수라고 한다.
    for i in range(n):
        num_list.append(int(sys.stdin.readline()))

    print(int(round(sum(num_list)/len(num_list),0)))    #첫번째 출력

    num_list.sort()
    print(num_list[int(len(num_list)/2)])               #두번째 출력


    num_cnt_dic = {string : 0 for string in num_list}
    for i in range(len(num_list)):
        num_cnt_dic[num_list[i]] = num_cnt_dic[num_list[i]] + 1

    dic_max_val = [i for i,y in num_cnt_dic.items() if max(num_cnt_dic.values()) == y]
    dic_max_val.sort()
    if len(dic_max_val) != 1:                               #세번째 출력
        print(dic_max_val[1])
    else:
        print(dic_max_val[0])

    if len(num_list) == 1:                              #네번째 출력
        print(0)
    else:
        print(num_list[-1] - num_list[0])