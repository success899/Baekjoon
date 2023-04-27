import sys
input=sys.stdin.readline

if_a, if_b, if_c, if_d = False, False, False, True

for _ in range(int(input())):
    a, b = map(int, input().split())

    if (a == 1 and b == 3) or (a == 3 and b == 1):
        if_a = True
    elif (a == 1 and b == 4) or (a == 4 and b == 1):
        if_b = True
    elif (a == 3 and b == 4) or (a == 4 and b == 3):
        if_c = True
    else:
        if_d = False


if if_a and if_b and if_c and if_d:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')