import sys, heapq
input=sys.stdin.readline

n = int(input())
heap = []

start = list(map(int, input().split())) 

for i in start:
    heapq.heappush(heap, i)

for i in range(n-1):  
    numbers = list(map(int, input().split())) 

    for j in numbers:
        if heap[0] < j :
            heapq.heappush(heap, j)
            heapq.heappop(heap)

print(heap[0])