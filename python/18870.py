import sys
input=sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))
X_set = list(set(X))
X_set.sort()
X_dic = {}

for i in range(len(X_set)):
    X_dic[X_set[i]] = i

for i in X:
    print(X_dic[i], end=' ')