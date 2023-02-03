from collections import deque
import sys
input=sys.stdin.readline

N = int(input())
num_list = deque(enumerate(map(int, input().split())))
pop_index = []


while num_list:
    index, pop_num = num_list.popleft()
    pop_index.append(index+1)

    if pop_num > 0:
        num_list.rotate(-(pop_num - 1))
    elif pop_num < 0:
        num_list.rotate(-pop_num)

for i in pop_index:
    print(i, end=' ')