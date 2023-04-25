import sys, re
input=sys.stdin.readline

for _ in range(int(input())):
    s, p = map(str, input().rstrip().split())
    result = re.sub(p,'1',s)

    print(len(result))