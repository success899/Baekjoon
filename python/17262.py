import sys
input=sys.stdin.readline

s_e_list = []
for _ in range(int(input())):
  s_e_list.append(list(map(int, input().split())))

a = sorted(s_e_list, key=lambda x: x[0])
b = sorted(s_e_list, key=lambda x: x[1])

result = a[-1][0] - b[0][1]

if result <= 0:
  print(0)
else :
  print(result)