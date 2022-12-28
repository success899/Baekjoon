import sys
input=sys.stdin.readline

for i in range(int(input())):
    score = list(map(int,input().split()))
    del score[0]
    score.sort()
    diff = []
    print('Class', i+1)
    for i in range(len(score)-1):
        diff.append(score[i+1] - score[i])

    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(diff)}')