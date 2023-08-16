import sys
input=sys.stdin.readline

N, B, H, W = map(int, input().split())
price, people, result = [], [], []

for i in range(H):
    price.append(int(input()))
    people.append(list(map(int, input().split())))

for i in range(H):
    for j in people[i]:
        if j > N:
            result.append(N * price[i])

if len(result) == 0:
    print('stay home')
elif min(result) > B:
    print('stay home')
else:
    print(min(result))