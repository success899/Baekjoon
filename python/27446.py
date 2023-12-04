import sys
input=sys.stdin.readline

N, M = map(int, input().split())
page_num = list(map(int, input().split()))
not_page = []

for i in range(1, N+1):
    if i not in page_num:
        not_page.append(i)

last = 0
result = 0
for i in not_page: 
    if last: 
        result += min(7, (i - last)*2)
    else:
        result += 7
    last = i

print(result)