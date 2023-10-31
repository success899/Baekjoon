import sys
input=sys.stdin.readline

N = int(input().rstrip())
t_list = list(map(int,input().rstrip().split()))
t_list.sort()

M = -int(1e9)

if len(t_list) % 2 == 0:
    for i in range(N // 2):
        M = max(t_list[i] + t_list[N-i-1], M)
    print(M)
else:
    for i in range((N-1) // 2):
        M = max(t_list[i] + t_list[N-i-2], M)
    print(max(M, t_list[-1]))