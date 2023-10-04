import sys
input=sys.stdin.readline

string = input().rstrip().replace('-', ' ')
words = string.split(' ')
front_word = ('c\'', 'j\'', 'n\'', 'm\'', 't\'', 's\'', 'l\'', 'd\'', 'qu\'', 's\'')
vowels = ('a', 'e', 'i', 'o', 'u', 'h')
word_count = len(words)

for word in words:
    if word.startswith(front_word):
        apo_idx = word.index("\'")
        apo_next = word[apo_idx+1]

        if apo_next in vowels:
            word_count += 1

print(word_count)