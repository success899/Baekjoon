import sys
input=sys.stdin.readline

N = int(input())
x_y = []

for _ in range(N):
    x,y = map(int,input().split())
    x_y.append([y, x])

x_y.sort()

for i in range(N):
  print(x_y[i][1],x_y[i][0])