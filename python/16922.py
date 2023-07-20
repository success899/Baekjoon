import sys
input=sys.stdin.readline

n = int(input())
roma_list = [1, 5, 10, 50]
result = set([0])

tmp = []
for _ in range(n):
    for i in result:
        for j in roma_list:
            tmp.append(i + j)
    result = set(tmp)
    tmp = []

print(len(result))