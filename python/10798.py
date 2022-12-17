import sys
input=sys.stdin.readline

input_str = []
max_length = 0
result = ''

for i in range(5):
    input_str.append(input().rstrip())
    if len(input_str[i]) >= max_length:
        max_length = len(input_str[i])

for j in range(max_length):
    for i in input_str:
        if len(i) < j + 1:
            continue
        else:
            result += i[j]

print(result)