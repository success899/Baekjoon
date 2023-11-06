import sys
input=sys.stdin.readline

N, K = map(int,input().split())
N_list = [int(input()) for _ in range(N)]

first = 1
last = max(N_list)
result = 0

while(first <= last):
    mid = (first+last)//2
    count = 0
    
    count = sum(i // mid for i in N_list)

    if count >= K:
        result = mid 
        first = mid + 1
    else:
        last = mid - 1
        
print(result)