import sys
input=sys.stdin.readline

X = int(input())
X_list = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in X_list:
    if X == 0:
        break
    elif X >= i:
        count += 1
        X -= i

print(count)