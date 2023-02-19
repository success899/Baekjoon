import sys
input=sys.stdin.readline

N = int(input())

start, end, count, sum = 0, 0, 0, 0

while end <= N:
    if sum < N:
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    elif sum == N:
        count += 1
        end += 1
        sum += end

print(count)