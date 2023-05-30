import sys
input=sys.stdin.readline

N = int(input())

start = 1
end = N

while start <= end:
    mid = (start+end) // 2
    if mid**2 == N:
        break
    elif mid**2 > N:
        end = mid
    else:
        start = mid
        
print(mid)