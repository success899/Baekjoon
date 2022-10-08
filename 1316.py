n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    er = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                er += 1
    if er == 0:  
        group_word += 1 
print(group_word)