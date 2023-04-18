import sys
input=sys.stdin.readline

N, M = map(int, input().split())
result = True

for _ in range(M):
    int(input())
    book_list = list(map(int, input().split()))
    sort_book_list = sorted(book_list, reverse=True)

    if book_list != sort_book_list:
        result = False
        break

if result:
    print('Yes')
else:
    print('No')