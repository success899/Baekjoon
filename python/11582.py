import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
k = int(input())
 
index = N // k
arr = []
 
for i in range(0, N, index):
    arr = N_list[i:i+index]
    arr.sort()
    for j in arr:
        print(j, end=' ')