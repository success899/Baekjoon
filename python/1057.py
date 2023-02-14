import sys
input=sys.stdin.readline

n, jimin, hansu = map(int, input().split())
count = 0

while True:
    if jimin == hansu:
        break
    jimin = jimin - (jimin // 2)
    hansu = hansu - (hansu // 2)
    count += 1

print(count)