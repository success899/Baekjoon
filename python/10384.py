import sys
input=sys.stdin.readline

for i in range(int(input())):
    text = input().upper().rstrip()
    tmp = [0] * 26

    for j in text:
        if j.isalpha():
            tmp[ord(j)-65] += 1

    if min(tmp) >= 3:
        print(f'Case {i+1}: Triple pangram!!!')
    elif min(tmp) == 2:
        print(f'Case {i+1}: Double pangram!!')
    elif min(tmp) == 1:
        print(f'Case {i+1}: Pangram!')
    else:
        print(f'Case {i+1}: Not a pangram')