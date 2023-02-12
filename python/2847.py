import sys
input=sys.stdin.readline

N = int(input())
score = []
count = 0

for _ in range(N):
    score.append(int(input()))

for i in range(N-1,0,-1):

    while True:
        if score[i-1] >= score[i]:
            score[i-1] -= 1
            count += 1
        else:
            break

print(count)