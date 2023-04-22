import sys, math
input=sys.stdin.readline

for _ in range(int(input())):
    letter = str(input().rstrip())
    letter_size_sqrt = int(math.sqrt(len(letter)))
    result = ''

    for i in range(letter_size_sqrt-1, -1, -1):
        for j in range(0, len(letter), letter_size_sqrt):
            tmp = letter[j:j+letter_size_sqrt]
            result += tmp[i]

    print(result)