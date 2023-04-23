import sys
input=sys.stdin.readline

word = str(input().rstrip())
answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word) ):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        reverse_a = a[::-1]
        reverse_b = b[::-1]
        reverse_c = c[::-1]
        answer.append(reverse_a + reverse_b + reverse_c)

answer.sort()

print(answer[0])