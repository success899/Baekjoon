import sys
input=sys.stdin.readline

toping = int(input())
toping_list = list(map(str, input().rstrip().split()))
toping_set = set(toping_list)
count = 0

if len(toping_set) < 4:
    print('sad')
else:
    for i in toping_set:
        if i[-6:] == 'Cheese':
            count += 1

    if count >= 4:
        print('yummy')
    else:
        print('sad')