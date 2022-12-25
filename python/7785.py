import sys
input=sys.stdin.readline

n = int(input())
gigle = dict()

for _ in range(n):
    name, state = map(str,input().split())
    
    if state == 'enter':
        gigle[name] = True
    
    if state == 'leave':
        del(gigle[name])

gigle = sorted(list(gigle.keys()), reverse=True)

print(' '.join(gigle))