import sys, heapq
input=sys.stdin.readline

N = int(input())
num_arr = []
result = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if len(num_arr) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(num_arr)[1])
    
    else:
        heapq.heappush(num_arr, (abs(x),x))
        
for i in result:
    print(i)