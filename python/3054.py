import sys
input=sys.stdin.readline

word = input().rstrip()
result = ['.', '.', '#', '.', '.']
for n, i in enumerate(word, 1):
    s = '#'
    if n % 3 == 0:
        s = '*'
        result[2] = result[2][:-1]+s
    result[0] += f'.{s}..'
    result[1] += f'{s}.{s}.'
    result[2] += f'.{i}.{s}'
    result[3] += f'{s}.{s}.'
    result[4] += f'.{s}..'

for i in result:
    print(i)