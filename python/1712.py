a,b,c = map(int,(input()).split())

num = 1

if b >= c:
    print("-1")
else:
    print(int(a/(c-b))+1)