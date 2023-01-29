import sys
input=sys.stdin.readline

N = int(input())
N_list = {}
max_book = []

for _ in range(N):
    book = str(input().rstrip())

    if book not in N_list:
        N_list[book] = 1
    elif book in N_list:
        N_list[book] = N_list.get(book)+1

max_num = max(N_list.values())

for i in N_list:
    if max_num == N_list[i]:
        max_book.append(i)
max_book.sort()

print(max_book[0])