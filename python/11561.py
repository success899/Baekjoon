import sys, math
input=sys.stdin.readline

c = -2 * int(1e16)
mx = int((-1 + math.sqrt(1-4*c)) // 2) + 1
 
T = int(input())
for _ in range(T):
    T -= 1
    N = int(input())
    s, e, result = 0, mx, 0
    while s < e:
        mid = (s+e) // 2
        if (mid+1) * mid // 2 <= N:
            result = mid
            s = mid + 1
        else:
            e = mid
    print(result)