import sys
input=sys.stdin.readline

N = int(input())
pattern_1, pattern_2 = str(input().rstrip()).split('*')
file_name = []

for _ in range(N):
    file_name.append(str(input().rstrip()))

for i in file_name:
    if len(i) >= (len(pattern_1) + len(pattern_2)):
        if pattern_1 == i[:len(pattern_1)] and pattern_2 == i[len(i)-len(pattern_2):]:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')