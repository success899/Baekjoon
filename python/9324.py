import sys
input=sys.stdin.readline

for _ in range(int(input())):
    M = str(input().rstrip())

    count = [0] * 26
    result, check = True, False

    for i in range(len(M)):
        if check:
            check = False
            continue
        
        count[ord(M[i]) - 65] += 1

        if count[ord(M[i]) - 65] == 3:
            if i == len(M) - 1:
                result = False
            elif M[i] != M[i+1]:
                result = False
            count[ord(M[i]) - 65] = 0
            check = True

    if result:
        print('OK')
    else:
        print('FAKE')