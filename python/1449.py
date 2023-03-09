import sys
input=sys.stdin.readline

N, L = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

start_tape = N_list[0] - 0.5
count = 1

for i in N_list[1:]:
    if start_tape + L < i + 0.5:
        start_tape = i - 0.5
        count += 1

print(count)