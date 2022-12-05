import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    costume_list = {}
    count = 1
    for _ in range(int(input())):
        costume_name, costume_type = map(str,input().split())

        if costume_type in costume_list.keys():
            costume_list[costume_type] += 1
        else:
            costume_list[costume_type] = 1

    for i in costume_list.keys():
        count *= costume_list[i]+1
    print(count-1)