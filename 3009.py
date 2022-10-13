import collections

x = []
y = []
for i in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)


count_x = collections.Counter(x)
count_y = collections.Counter(y)
print(count_x.most_common()[-1][0],count_y.most_common()[-1][0])