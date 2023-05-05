import sys
input=sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    page_list = [0] * (N+1)
    print_page = list(map(str, input().rstrip().split(',')))

    for page in print_page:
        if '-' not in page:
            start, end = int(page), int(page)
        else:
            start, end = map(int, page.split('-'))

        if start <= end:
            for i in range(start, end+1):
                if i <= N:
                    page_list[i] = 1

    print(sum(page_list))