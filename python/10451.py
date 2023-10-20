import sys
input=sys.stdin.readline

def solution(n):
    visited[n] = 1
    tmp = arr[n]
    if visited[tmp] == 0:
        solution(tmp)
    return

arr = [0]

for _ in range(int(input())):
    count = 0
    n = int(input())
    visited = [0] * (n + 1)
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    for i in range(1, n + 1):
        if visited[i] == 0:
            solution(i)
            count += 1
            
    print(count)