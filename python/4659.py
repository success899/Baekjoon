import sys
input=sys.stdin.readline

while True:
    password = str(input().rstrip())
    count_1 = 0     #조건1 해당되는지 판단
    count_2_1 = 1   #조건2 모음
    count_2_2 = 1   #조건2 자음
    count_3 = 1     #조건3 해당되는지 판단

    if password == 'end':
        break

    for i in range(len(password)):
        if password[i] in 'aeiou':
            count_1 = 1
    
        if i >= 1:
            if password[i] == password[i-1] and password[i] != 'e' and password[i] != 'o':
                count_3 = 0
        
        if i >= 2:
            if password[i] in 'aeiou' and password[i-1] in 'aeiou' and password[i-2] in 'aeiou':
                count_2_1 = 0
            elif password[i] not in 'aeiou' and password[i-1] not in 'aeiou' and password[i-2] not in 'aeiou':
                count_2_2 = 0
        
    
    if count_1 == 1 and count_2_1 == 1 and count_2_2 == 1 and count_3 == 1:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")