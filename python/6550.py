import sys
input=sys.stdin.readline

while True:
    try:
        s, t = map(str, input().rstrip().split())
        index = 0
        right = 0

        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
                if index == len(s):
                    right = 1
                    break
        
        if right == 1:
            print('Yes')
        else:
            print('No')

    except:
        break