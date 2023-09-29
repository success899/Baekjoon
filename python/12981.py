import sys
input=sys.stdin.readline

R, G, B = map(int, input().split())

min_box = min(R,G,B)
result = min_box
R -= min_box
G -= min_box
B -= min_box

result += R//3 + G//3 + B//3
R %= 3
G %= 3
B %= 3

if R == 2:
  result += 1
  R = 0
if G == 2:
  result += 1
  G = 0
if B == 2:
  result += 1
  B = 0

if R+G+B > 0:
  result += 1
  
print(result)