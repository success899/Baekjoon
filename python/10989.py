import sys

N = int(sys.stdin.readline())

N_list = [0] * 10001

for _ in range(N):
    input_num = int(sys.stdin.readline())
    
    N_list[input_num] = N_list[input_num] + 1
    
for i in range(10001):
    if N_list[i] != 0:
        for _ in range(N_list[i]):
            print(i)