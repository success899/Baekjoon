import sys, re
input=sys.stdin.readline

words, result = [], []

while True:
    words.extend(input().rstrip().split())
    if words[-1] == 'E-N-D': 
        break

for i in words:
    result.append(re.sub('[^a-z-]','', i.lower()))
result.sort(key=len, reverse=True)

print(result[0])