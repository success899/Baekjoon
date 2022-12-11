import sys, heapq
input=sys.stdin.readline

N = int(input())
num_arr = []
result = []

#heappush 에서 -1을 곱해서 넣는 방식으로 해당 문제에서 요구하는 입력 값을 음수로 만들어
#가장 큰 수를 작은 수로 보이게 만드는 방법을 사용하여 최소힙을 구하고 값을 가져올 때
#다시 -1을 곱하여 원래 수로 만듬
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(num_arr) == 0:
            result.append(0)
        else:
            result.append(-1 * heapq.heappop(num_arr))
    
    else:
        heapq.heappush(num_arr, -1*x)
        
for i in result:
    print(i)