import sys
input=sys.stdin.readline

string = str(input().rstrip())
word = str(input().rstrip())
count = 0
index = 0

while True:
    if len(word) > len(string[index:]):
        break

    tmp = string[index:].find(word)

    if tmp == -1:
        break
    else:
        index = index + tmp + len(word)
        count += 1

print(count)