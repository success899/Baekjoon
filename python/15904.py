import sys
input=sys.stdin.readline

string = str(input().rstrip())
find_str = ['U', 'C', 'P', 'C']
index, count = 0, 0

for i in find_str:
    if string[index:].find(i) != -1:
        index += string[index:].find(i)
        count += 1
    else:
        break

if count == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')