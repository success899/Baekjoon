import sys
input=sys.stdin.readline

for _ in range(int(input())):
    words = []
    tmp = []
    k = int(input())

    for _ in range(k):
        words.append(str(input().rstrip()))

    for i in range(k):
        for j in range(k):
            if i != j:
                tmp.append(words[i] + words[j])

    for i in tmp:
        if i == i[::-1]:
            print(i)
            break
    else:
        print(0)