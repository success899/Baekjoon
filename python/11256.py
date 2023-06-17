import sys
input=sys.stdin.readline

for _ in range(int(input())):
    candy, box = map(int, input().split())
    size = []
    result, tmp = 0, 0
    for _ in range(box):
        tmp1, tmp2 = map(int, input().split())
        size.append(tmp1 * tmp2)
    size.sort(reverse=True)

    for i in size:
        tmp += i
        result += 1
        if tmp >= candy:
            print(result)
            break