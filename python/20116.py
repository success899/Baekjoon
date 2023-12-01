import sys
input=sys.stdin.readline

n, L = map(int, input().split())
X_list = list(map(int, input().split()))
sum = 0

for i in range(n-1, 0, -1):
    sum += X_list[i]
    tmp = sum / (n-i)

    if tmp <= X_list[i-1] - L or tmp >= X_list[i-1] + L:
        print("unstable")
        exit()

print("stable")