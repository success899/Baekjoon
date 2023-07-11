import sys
input=sys.stdin.readline

for i in range(int(input())):
    num = int(input())
    result = 0

    for j in range(2,65):
        tmp_list = []
        tmp = num

        while tmp != 0:
            tmp_list.append(tmp%j)
            tmp = tmp//j

        for k in range(len(tmp_list)//2):
            if tmp_list[k] != tmp_list[-1-k]:
                result += 1
                break
    if result == 63:
        print(0)
    else:
        print(1)