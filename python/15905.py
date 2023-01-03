import sys
input=sys.stdin.readline

ranking = []
count = 0
index = 5

for _ in range(int(input())):
    ranking.append(list(map(int, input().split())))

ranking.sort(key=lambda x: (-x[0], x[1]))

while True:
    if len(ranking) == index or ranking[index-1][0] != ranking[index][0]:
        print(count)
        break
    count += 1
    index += 1