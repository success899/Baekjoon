import sys
input=sys.stdin.readline

word_list = []

for _ in range(int(input())):
    tmp = str(input().rstrip())
    tmp = ''.join(sorted(tmp))
    word_list.append(tmp)

word_list = set(word_list)
print(len(word_list))