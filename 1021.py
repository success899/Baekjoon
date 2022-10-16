from collections import deque

n, m = map(int, input().split())
s = list(map(int ,input().split()))
num_list = deque([])
cnt = 0

for i in range(n):
    num_list.append(i+1)

for num in s:
    while True:
        if num_list[0] == num:
            num_list.popleft()
            break
        else:
            if num_list.index(num) <= len(num_list)//2:
                num_list.rotate(-1)
                cnt += 1
            else:
                num_list.rotate(1)
                cnt += 1

print(cnt)