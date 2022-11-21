import sys
input=sys.stdin.readline

N = int(input())
x_y = []

for _ in range(N):
    x_y.append(list(map(int,input().split())))

x_y.sort()

for i in range(N):
  print(x_y[i][0],x_y[i][1])