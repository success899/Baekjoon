import sys
input=sys.stdin.readline

N = int(input())
N_list = []

for _ in range(N):
    name, korean, english, math = map(str, input().split())
    korean, english, math = int(korean), int(english), int(math)
    N_list.append([korean, english, math, name])
N_list.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for i in range(N):
    print(N_list[i][3])