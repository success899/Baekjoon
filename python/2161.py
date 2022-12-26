import sys
input=sys.stdin.readline

N = int(input())

num_list = [ num for num in range(1,N+1) ]

while True:
    print(num_list[0], end=' ')
    del num_list[0]

    if len(num_list) == 0:
        break

    num_list.append(num_list[0])
    del num_list[0]