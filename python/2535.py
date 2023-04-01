import sys
input=sys.stdin.readline

N = int(input())
N_list = []

for _ in range(N):
    N_list.append(list(map(int, input().split())))

N_list.sort(key=lambda x: -x[2])

print(N_list[0][0], N_list[0][1])
print(N_list[1][0], N_list[1][1])
index = 2
while True:
    if N_list[index][0] == N_list[0][0]:
        index += 1
    else:
        print(N_list[index][0], N_list[index][1])
        break