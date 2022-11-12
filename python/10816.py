from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
count = Counter(N_list)

M = int(input())
M_list = list(map(int,input().split()))

for i in range(M):
    if M_list[i] in count:
        print(count[M_list[i]],end=' ')
    else:
        print(0,end=' ')