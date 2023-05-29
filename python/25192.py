import sys
input=sys.stdin.readline

result = set()
count = 0

for _ in range(int(input())):

    word = input().rstrip()

    if word != 'ENTER':
        if word not in result:
            count += 1
            result.add(word)
    elif word == 'ENTER':
            result.clear()

print(count)